import dtcli.building
import dtcli.constants
import dtcli.server_api
import typer
from typing_extensions import Annotated
import pandas as pd
from dynatrace import Dynatrace
from dynatrace.environment_v2.extensions import MonitoringConfigurationDto
from dynatrace.http_client import TOO_MANY_REQUESTS_WAIT
from rich.progress import track
from rich import print
import yaml
import dtcli
from typing import Optional, List, Dict
import json
import logging
from pathlib import Path

class MyDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)

from .models import CustomDBQuery
from .db_conversion import (
    EF2SqlExtension,
    queries_from_ef1_config,
)
from .utils import (
    build_dt_custom_device_id,
    build_dt_group_id,
    dt_murmur3,
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

EF1_EXTENSION_ID = "custom.remote.python.dbquery"
TIMEOUT = 120
TIMEFRAME = "now-6M"

app = typer.Typer()


@app.command(help="Pull EF1 db queries configurations into a spreadsheet.")
def pull(
    dt_url: Annotated[str, typer.Option(envvar="DT_URL")],
    dt_token: Annotated[str, typer.Option(envvar="DT_TOKEN")],
    output_file: Optional[str] = None or f"{EF1_EXTENSION_ID}-export.xlsx",
):
    dt = Dynatrace(
        dt_url,
        dt_token,
        too_many_requests_strategy=TOO_MANY_REQUESTS_WAIT,
        retries=3,
        log=logger,
        timeout=TIMEOUT,
    )
    configs = list(dt.extensions.list_instances(extension_id=EF1_EXTENSION_ID))
    all_queries: List[CustomDBQuery] = []
    full_configs = []

    for config in track(configs, description="Pulling EF1 configs"):
        config = config.get_full_configuration(EF1_EXTENSION_ID)
        full_config = config.json()
        properties = full_config.get("properties", {})

        group_name = properties.get("group_name") or "Custom DB Queries Group"
        device_name = properties.get("custom_device_name") or "Custom DB Queries Device"
        group_id = dt_murmur3(build_dt_group_id(group_name))
        device_id = f"CUSTOM_DEVICE-{dt_murmur3(build_dt_custom_device_id(group_id, device_name))}"

        full_config.update(
            {
                "device_id": device_id,
                "database_type": properties["database_type"],
                "group_name": properties["group_name"],
                "database_host": properties["database_host"],
                "database_name": properties["database_name"],
                "database_username": properties["database_username"],
                "custom_device_name": properties["custom_device_name"],
            }
        )

        configured_queries = queries_from_ef1_config(full_config["properties"])
        all_queries.extend(configured_queries)
        full_config.update({"queries": len(configured_queries)})
        full_config["properties"] = json.dumps(properties)
        full_configs.append(full_config)

    print("Finished pulling configs...")
    print("Adding data to document...")
    writer = pd.ExcelWriter(
        output_file,
        engine="xlsxwriter",
    )
    df = pd.DataFrame(full_configs)
    df.to_excel(writer, "Endpoints", index=False, header=True)

    df_queries = pd.DataFrame({"queries": [query.value for query in all_queries]})
    df_queries.to_excel(writer, "Queries", index=False, header=True)

    print("Closing document...")
    writer.close()
    print(f"Exported configurations available in '{output_file}'")


@app.command(help="Build EF2 SQL extensions from DB queries configuration export")
def build(
    dt_url: Annotated[str, typer.Option(envvar="DT_URL")],
    dt_token: Annotated[str, typer.Option(envvar="DT_TOKEN")],
    cert_file_path: Annotated[str, typer.Option()],
    private_key_path: Annotated[str, typer.Option()],
    input_file: Optional[str] = None or f"{EF1_EXTENSION_ID}-export.xlsx",
    directory: Optional[str] = "migrated_extensions",
    merge_endpoints: Optional[bool] = False,
    credential_vault_id: Optional[str] = None,
    upload: Optional[bool] = False,
    create_config: Optional[bool] = False,
    scope: Optional[str] = "ag_group-default",
    pre_cron: Optional[bool] = False
):

    if scope and not scope.startswith("ag_group-"):
        scope = f"ag_group-{scope}"

    dt = Dynatrace(
        dt_url,
        dt_token,
        too_many_requests_strategy=TOO_MANY_REQUESTS_WAIT,
        retries=3,
        log=logger,
        timeout=TIMEOUT,
    )

    xls = pd.ExcelFile(input_file)
    df = pd.read_excel(xls, "Endpoints")

    if merge_endpoints:

        grouped_endpoints: Dict[str, List] = {}

        for index, row in df.iterrows():
            config_props = json.loads(row["properties"], strict=False)
            host = config_props.get("database_host")
            database = config_props.get("database_name")
            jdbc_string = config_props.get("jdbc_connection_string")

            if host and database:
                identifier = f"{host}_{database}"
            elif host:
                identifier = f"{host}"
            elif jdbc_string:
                identifier = f"{jdbc_string}"
            else:
                print(f"Potentially broken config: host: {host}, database: {database}, jdbc: {jdbc_string}")
            
            if grouped_endpoints.get(identifier):
                grouped_endpoints[identifier].append(config_props)
            else:
                grouped_endpoints[identifier] = [config_props]
        
        for group in track(grouped_endpoints):
            try:
                ext = EF2SqlExtension(dt, group, grouped_endpoints[group], credential_vault_id, pre_cron)
                extension_file = Path(directory, f"{ext.name.replace(':', '_')}", "src", "extension.yaml")
                extension_file.parent.mkdir(parents=True, exist_ok=True)
                extension_file.write_text(yaml.dump(ext.dictionary, sort_keys=False, Dumper=MyDumper, default_flow_style=False))
                activation_file = Path(directory, f"{ext.name.replace(':', '_')}", f"activation.json")
                activation_file.write_text(json.dumps(ext.activation_config))
                extension_zip = Path(extension_file.parent, dtcli.constants.EXTENSION_ZIP)
                dtcli.building.build_and_sign(extension_dir_path=extension_file.parent, extension_zip_path=extension_zip, 
                                            extension_zip_sig_path=Path(extension_file.parent.parent, dtcli.constants.EXTENSION_ZIP_SIG).absolute(), certificate_file_path=cert_file_path, private_key_file_path=private_key_path,
                                            target_dir_path=extension_file.parent.parent)
                
                built_extension_zip = Path(extension_file.parent.parent, f"{ext.name.replace(':', '_')}-{ext.version}.zip".replace(":", "_"))

                dtcli.server_api.validate(extension_zip_file=built_extension_zip, tenant_url=dt_url, api_token=dt_token)

                if upload:
                    dtcli.server_api.upload(extension_zip_file=built_extension_zip, tenant_url=dt_url, api_token=dt_token)
                    dt.extensions_v2.put_environment_config(extension_name=ext.name, extension_version=ext.version)
                if create_config:
                    print("Creating configuration...")
                    dt.extensions_v2.post_monitoring_configurations(ext.name, [MonitoringConfigurationDto(scope=scope, configuration=ext.activation_config)])
            except Exception as e:
                print(f"Error handling group {group}: {e}")
            
        return
    
    else:
        for index, row in track(df.iterrows()):
            try:
                config_props = json.loads(row["properties"])
                ext = EF2SqlExtension(dt, row["endpointName"], config_props, credential_vault_id, pre_cron)
                extension_file = Path(directory, f"{ext.name.replace(':', '_')}", "src", "extension.yaml")
                extension_file.parent.mkdir(parents=True, exist_ok=True)
                extension_file.write_text(yaml.safe_dump(ext.dictionary, sort_keys=False))
                activation_file = Path(directory, f"{ext.name.replace(':', '_')}", f"activation.json")
                activation_file.write_text(json.dumps(ext.activation_config))
                extension_zip = Path(extension_file.parent, dtcli.constants.EXTENSION_ZIP)
                dtcli.building.build_and_sign(extension_dir_path=extension_file.parent, extension_zip_path=extension_zip, 
                                            extension_zip_sig_path=Path(extension_file.parent.parent, dtcli.constants.EXTENSION_ZIP_SIG).absolute(), certificate_file_path=cert_file_path, private_key_file_path=private_key_path,
                                            target_dir_path=extension_file.parent.parent)
                built_extension_zip = Path(extension_file.parent.parent, f"{ext.name.replace(':', '_')}-{ext.version}.zip".replace(":", "_"))
                dtcli.server_api.validate(extension_zip_file=built_extension_zip, tenant_url=dt_url, api_token=dt_token)
                if upload:
                    dtcli.server_api.upload(extension_zip_file=built_extension_zip, tenant_url=dt_url, api_token=dt_token)
                    dt.extensions_v2.put_environment_config(extension_name=ext.name, extension_version=ext.version)
                if create_config:
                    print("Creating configuration...")
                    dt.extensions_v2.post_monitoring_configurations(ext.name, [MonitoringConfigurationDto(scope=scope, configuration=ext.activation_config)])
            except Exception as e:
                print(f"Error handling endpoint {row['endpointName']}: {e}")


if __name__ == "__main__":
    app()
