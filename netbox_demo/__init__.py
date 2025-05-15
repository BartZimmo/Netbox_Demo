from extras.plugins import PluginConfig


class NetBoxDemoConfig(PluginConfig):
    name = 'netbox_Demo'
    verbose_name = ' NetBox Demo Plugin'
    description = 'Learn how to make a netbox plugin'
    version = '0.1'
    base_url = 'Demo'
    min_version = '4.2.0'


config = NetBoxDemoConfig
