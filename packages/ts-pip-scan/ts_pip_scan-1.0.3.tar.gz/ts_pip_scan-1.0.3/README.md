# TrustSource-pip-scan

TrustSource plugin for scanning python project install pip dependencies and uploading them https://app.trustsource.io for code compliance evaluation 
This package came about because official TrustSource provided packages ([ts-pip-plugin](https://github.com/TrustSource/ts-pip-plugin), [ts-python-client](https://github.com/TrustSource/ts-python-client)) and  either don't work as of this time or don't provide good integration in the CI/CD pipelines for python projects.
The library is influenced by [ts-pip-plugin](https://github.com/TrustSource/ts-pip-plugin)

This plugin is geared towards the use in CI/CD pipelines. It can do legal and vulnerability evaluation after TrustSource analysed the scan results. 
The package command exist with code 1 if evaluation fails.


## Installation

### Installation from pip

```
    pip install ts-pip-scan
```

### Installing it from local dir

```
git clone https://github.com/JoeMabor/TrustSource-pip-scan.git

pip install <path>/TrustSource-pip-scan

```
 

## Usage

TrustSource project and api key can be provided as options in the commandline or ts-plugin.json that can be added to root dir of the project to be scanned.
Content of ts-plugin.json

```
{
    "project": "<TrustSource Project Name>",
    "apiKey": "<api-key>",
    base_url: str = TS_API_URL
    max_legal_warnings: 0
    max_legal_violations: 0
    max_vulnerability_warning: 0
    max_vulnerability_violations: 0
    skip_upload: false
    
}

```
Scan dependencies and upload them to TrustSource 
```
ts-pip-scan scan <path-to-project-being-scanned/
```
Scan dependencies, upload to TrustSource and evaluate legal and vulnerability analysis
```
ts-pip-scan scan -val <path-to-project-being-scanned/
```
Scan dependencies without uploading results

```
ts-pip-scan scan --skip-upload <path-to-project-being-scanned/
```

For info about options, run 

```
ts-pip-scan --help
ts-pip-scan scan --help
```

Some configs can be set as environment variables

    max_legal_warnings -> TS_MAX_LEGAL_WARNINGS
    max_legal_violations -> TS_MAX_LEGAL_VIOLATIONS
    max_vulnerability_warnings -> TS_MAX_VULNERABILITY_WARNINGS
    max_vulnerability_violations -> TS_MAX_VULNERABILITY_VIOLATIONS
    TS_SKIP_UPLOAD -> skip_upload