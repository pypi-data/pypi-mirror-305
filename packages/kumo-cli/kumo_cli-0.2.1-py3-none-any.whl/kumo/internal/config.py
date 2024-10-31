from typing import Dict

from kumo.model.config.base import KumoBaseConfig
from kumo.model.config.builder import KumoBuilderConfig
from kumo.model.config.proxy import KumoProxyConfig
from kumo.model.config.registry import KumoRegistryConfig
from kumo.model.config.role import KumoRoleConfig
from kumo.model.config.ssh import KumoSSHConfig


class KumoConfig(KumoBaseConfig):

    app_name: str
    image: str
    role: Dict[str, KumoRoleConfig]
    builder: KumoBuilderConfig
    ssh: KumoSSHConfig
    registry: KumoRegistryConfig
    proxy: KumoProxyConfig
