from netbox.plugins import PluginConfig


class NetBoxDemoConfig(PluginConfig):
    name = 'netbox_demo'
    verbose_name = ' NetBox Demo Plugin'
    description = 'Learn how to make a netbox plugin'
    version = '0.1'
    base_url = 'demo'
    min_version = '4.2.0'
    author = 'Bart VdB'
    author_email = 'bart@zimmo.be'


config = NetBoxDemoConfig
