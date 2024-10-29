import json
import os
import pathlib
import click

from ts_pip_scan.models import Config, TS_API_URL
from ts_pip_scan.scanner import Scanner

def load_config(base_dir):
    path = os.path.join(base_dir, "ts-plugin.json")
    if os.path.exists(path):

        with open(path, "r") as config_file:
            return json.load(config_file)
    print(f"{path} not found")
    return {}

@click.group()
def cli():
    pass

@cli.command()
@click.option("-u","--base-url", "base_url", default=TS_API_URL, help='TrustSource API base URL')
@click.option("-p","--project", "project", default=None, help='Name of the project in TrustSource to which scanned results are sent via TrustSource API')
@click.option("-m","--module", "module", default=None, help='Name of the project to be scanned. If not provided, base folder name is used')
@click.option("-ak","--api-key", "api_key", default=None, help='API key for TrustSource API')
@click.option("-eval","--evaluate", "evaluate", is_flag=True, help='Evaluate legal and vulnerability warning and violations found by TrustSource')
@click.option("-su","--skip-upload", "skip_upload", is_flag=True, help='Skip upload and evaluation of scan results')
@click.option("-o","--output", "output", type=click.Path(path_type=pathlib.Path), help='Path or file to write scan and evaluation results')
@click.argument('path', type=click.Path(exists=True, path_type=pathlib.Path))
def scan(base_url, project,module, api_key, evaluate,skip_upload, output, path: pathlib.Path):
    click.echo("Scanning for dependencies...")
    path = path.resolve()
    config_dict = load_config(path)
    if api_key:
        config_dict["apiKey"] = api_key
    if module:
        config_dict["module"] = module
    if project:
        config_dict["project"] = project
    config_dict["base_url"] = base_url.rstrip("/")
    config_dict["skip_upload"] = skip_upload
    config = Config(**config_dict)

    scanner = Scanner(path, config)
    scanner.scan(evaluate=evaluate, output=output)
