class PluginInfo:
    """插件信息类"""
    
    def __init__(self):
        self.id = None
        self.name = None
        self.version = None
        self.type = None
        self.description = None
        self.status = None
        self.supported_commands = []
        self.supported_events = []
        
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_version(self):
        return self.version
    
    def set_version(self, version):
        self.version = version
        
    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type
        
    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
        
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status
        
    def get_supported_commands(self):
        return self.supported_commands
    
    def set_supported_commands(self, supported_commands):
        self.supported_commands = supported_commands
        
    def add_supported_command(self, command):
        self.supported_commands.append(command)
        
    def get_supported_events(self):
        return self.supported_events
    
    def set_supported_events(self, supported_events):
        self.supported_events = supported_events
        
    def add_supported_event(self, event):
        self.supported_events.append(event)