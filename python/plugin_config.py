class PluginConfig:
    """插件配置类"""
    
    def __init__(self):
        self.server_host = None
        self.server_port = None
        self.plugin_id = None
        self.plugin_name = None
        self.plugin_version = None
        self.plugin_type = None
        self.additional_config = {}
        
    def get_server_host(self):
        return self.server_host
    
    def set_server_host(self, server_host):
        self.server_host = server_host
        
    def get_server_port(self):
        return self.server_port
    
    def set_server_port(self, server_port):
        self.server_port = server_port
        
    def get_plugin_id(self):
        return self.plugin_id
    
    def set_plugin_id(self, plugin_id):
        self.plugin_id = plugin_id
        
    def get_plugin_name(self):
        return self.plugin_name
    
    def set_plugin_name(self, plugin_name):
        self.plugin_name = plugin_name
        
    def get_plugin_version(self):
        return self.plugin_version
    
    def set_plugin_version(self, plugin_version):
        self.plugin_version = plugin_version
        
    def get_plugin_type(self):
        return self.plugin_type
    
    def set_plugin_type(self, plugin_type):
        self.plugin_type = plugin_type
        
    def get_additional_config(self):
        return self.additional_config
    
    def set_additional_config(self, additional_config):
        self.additional_config = additional_config
        
    def add_config(self, key, value):
        self.additional_config[key] = value
        
    def get_config(self, key):
        return self.additional_config.get(key)