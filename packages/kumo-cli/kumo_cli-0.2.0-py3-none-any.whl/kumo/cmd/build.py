import subprocess

import typer
import yaml

from kumo.internal.config import KumoConfig
from kumo.internal.logger import KumoLogger
from kumo.utils.common import get_versioning

logger = KumoLogger(__name__)

build_app = typer.Typer(
    add_completion=False,
    no_args_is_help=False,
    name="build",
    help="Faz o build do projeto",
    invoke_without_command=True,
)


@build_app.callback(invoke_without_command=True)
def build_callback(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        run()


def run():
    typer.echo("Executando o build...")
    # cmd = "docker buildx create --name kumo-local --driver docker-container --platform=linux/amd64,linux/arm64"
    # use = "docker buildx use kumo-local"

    # Exemplo de execução de validação
    try:
        config_data = load_and_validate_yaml(".kumo/config/deploy.yaml")
        logger.info("Configuração YAML válida:")
        # _ver = get_versioning(config_data)
        # print(_ver)
        # logger.info(f"Versão: {_ver}")
    except Exception as e:
        logger.error("Erro ao validar a configuração YAML:", e)
        
    print(config_data['builder'].get("versioning", "tag"))


def load_and_validate_yaml(file_path: str) -> KumoConfig:
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
        return (data)
        # return KumoConfig(**data)


def create():
    # cmd = "docker buildx create --name kumo-local1 --driver=docker-container --platform=linux/amd64,linux/arm64"
    output = subprocess.check_output(
        [
            "docker",
            "buildx",
            "create",
            "--name",
            "kumo-local",
            "--platform",
            "linux/amd64,linux/arm64",
        ]
    )
    print(output)


def use():
    output = subprocess.check_output(["docker", "buildx", "use", "kumo-local-1"])
    print(output)


def remove():
    output = subprocess.check_output(["docker", "buildx", "rm", "kumo-local"])
    print(output)


