from netbox.plugins import PluginConfig

class NetboxDataConfig(PluginConfig):
    name = 'netbox_data'
    verbose_name = 'Netbox Data'
    description = 'Get netbox data'
    version = '1.1.0'
    base_url = 'netbox-data'
    min_version = '4.0.9'

config = NetboxDataConfig
