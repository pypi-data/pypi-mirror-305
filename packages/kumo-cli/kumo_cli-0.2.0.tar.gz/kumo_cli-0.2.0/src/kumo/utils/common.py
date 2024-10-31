import subprocess
from datetime import datetime
import yaml


# Função para obter o hash do commit do git
def get_git_commit_hash() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()


# Função para obter a tag atual do git (se houver)
def get_git_tag() -> str:
    try:
        return subprocess.check_output(["git", "describe", "--tags"]).decode().strip()
    except subprocess.CalledProcessError:
        return str(None)

# Função para obter o versionamento correto
def get_versioning(config_data: dict) -> str:
    # versioning = config_data['builder'].get('versioning', 'timestamp')
    versioning = config_data['builder']
    print(versioning)
    
    if versioning == 'timestamp':
        print(versioning)
        return datetime.now().strftime('%Y%m%d%H%M%S')
    elif versioning == 'hash':
        return get_git_commit_hash()
    elif versioning == 'tag':
        tag = get_git_tag()
        if not tag:
            raise ValueError("Nenhuma tag encontrada no repositório Git.")
        return tag
    else:
        raise ValueError(f"Tipo de versionamento desconhecido: {versioning}")

# Função para ler o arquivo YAML
def read_config(config_file: str) -> dict:
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)