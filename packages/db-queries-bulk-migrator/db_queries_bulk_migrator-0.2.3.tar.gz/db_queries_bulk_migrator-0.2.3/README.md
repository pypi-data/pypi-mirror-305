# Dynatrace DB Queries Extension Bulk Migrator

Tool to help with creating Extensions 2.0 declarative SQL extensions off of Extensions 1.0 Custom DB Queries extension configurations.

## API Authentication

For commands that interact with the Dynatrace API you need to provide an API URL and Access token. These can be provided on the command line but it is recommended to use environment variables:

- DT_URL (e.g. https://xxx.live.dynatrace.com)
- DT_TOKEN
  - permissions:
    - ReadConfig
    - WriteConfig
    - extensions.read
    - extensions.write
    - metrics.read

## Commands

Use `--help` with any command to view unique options.

```
 Usage: dbqm pull [OPTIONS]

 Pull EF1 db queries configurations into a spreadsheet.

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --dt-url             TEXT  [env var: DT_URL] [default: None] [required]                                                                                                                                                                                         │
│ *  --dt-token           TEXT  [env var: DT_TOKEN] [default: None] [required]                                                                                                                                                                                       │
│    --output-file        TEXT  [default: custom.remote.python.dbquery-export.xlsx]                                                                                                                                                                                  │
│    --help                     Show this message and exit.  
```

### dbqm pull

Used to pull all EF1 Custom DB Queries configurations and export them to an Excel sheet for manual review and as an input to later steps.

### dbqm build

Used to build extensions from a previously exported configuration excel workbook.

#### Certificate and key

Before building you need to create a developer key and certificate. These will be used to sign the extension packages. Refer to the steps [here](https://docs.dynatrace.com/docs/shortlink/sign-extension#cert) for creating the certificate and key file(s). The `developer.pem` file will be used in the build command.

#### Required options

- `--cert-file-path` path to developer.pem
- `--private-key-path` path to developer.pem
- `--input-file` path to the previously exported configuration exce;
- `--merge-endpoints` tells the tool to merge endpoints based on a matching host or jdbc string (to avoid hitting limits if it were one extension per EF1 DB queries endpoint)
- `--directory` path to where the migrated extensions will be stored locally
- `--upload` upload and activate extensions after build
- `--create-config` create an initial monitoring configuration based on the db queries configuration (in a disabled state)
- `--pre-cron` set this if you are waiting to update AG to 1.301, by default it will set the cron schedule in the new extension but this is only available in AG 1.301+
- `--scope` sets the AG group any created configs will be assigned. If not prefixed with 'ag_group-' this will be added automatically (default: 'ag_group-default)

Example:

```
dbqm build --cert-file-path=developer.pem --private-key-path=developer.pem  --input-file=custom.remote.python.dbquery-export.xlsx --merge-endpoints --directory=C:\workspaces\migrated_extensions
```

After running in the directory (default: migrated_extensions) you will see a directory per new extension which will contain a src directory and a signed zip of the new extension.
