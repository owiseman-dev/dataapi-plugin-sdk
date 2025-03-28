/// 插件信息结构体
#[derive(Debug, Clone)]
pub struct PluginInfo {
    id: String,
    name: String,
    version: String,
    plugin_type: String,
    description: String,
    status: String,
    supported_commands: Vec<String>,
    supported_events: Vec<String>,
}

impl PluginInfo {
    pub fn new() -> Self {
        Self {
            id: String::new(),
            name: String::new(),
            version: String::new(),
            plugin_type: String::new(),
            description: String::new(),
            status: String::new(),
            supported_commands: Vec::new(),
            supported_events: Vec::new(),
        }
    }

    pub fn get_id(&self) -> &str {
        &self.id
    }

    pub fn set_id(&mut self, id: String) {
        self.id = id;
    }

    pub fn get_name(&self) -> &str {
        &self.name
    }

    pub fn set_name(&mut self, name: String) {
        self.name = name;
    }

    pub fn get_version(&self) -> &str {
        &self.version
    }

    pub fn set_version(&mut self, version: String) {
        self.version = version;
    }

    pub fn get_type(&self) -> &str {
        &self.plugin_type
    }

    pub fn set_type(&mut self, plugin_type: String) {
        self.plugin_type = plugin_type;
    }

    pub fn get_description(&self) -> &str {
        &self.description
    }

    pub fn set_description(&mut self, description: String) {
        self.description = description;
    }

    pub fn get_status(&self) -> &str {
        &self.status
    }

    pub fn set_status(&mut self, status: String) {
        self.status = status;
    }

    pub fn get_supported_commands(&self) -> &Vec<String> {
        &self.supported_commands
    }

    pub fn set_supported_commands(&mut self, supported_commands: Vec<String>) {
        self.supported_commands = supported_commands;
    }

    pub fn add_supported_command(&mut self, command: String) {
        self.supported_commands.push(command);
    }

    pub fn get_supported_events(&self) -> &Vec<String> {
        &self.supported_events
    }

    pub fn set_supported_events(&mut self, supported_events: Vec<String>) {
        self.supported_events = supported_events;
    }

    pub fn add_supported_event(&mut self, event: String) {
        self.supported_events.push(event);
    }
}