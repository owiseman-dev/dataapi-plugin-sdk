use std::collections::HashMap;

/// 插件配置结构体
#[derive(Debug, Clone)]
pub struct PluginConfig {
    server_host: String,
    server_port: i32,
    plugin_id: String,
    plugin_name: String,
    plugin_version: String,
    plugin_type: String,
    additional_config: HashMap<String, String>,
}

impl PluginConfig {
    pub fn new() -> Self {
        Self {
            server_host: String::new(),
            server_port: 0,
            plugin_id: String::new(),
            plugin_name: String::new(),
            plugin_version: String::new(),
            plugin_type: String::new(),
            additional_config: HashMap::new(),
        }
    }

    pub fn get_server_host(&self) -> &str {
        &self.server_host
    }

    pub fn set_server_host(&mut self, server_host: String) {
        self.server_host = server_host;
    }

    pub fn get_server_port(&self) -> i32 {
        self.server_port
    }

    pub fn set_server_port(&mut self, server_port: i32) {
        self.server_port = server_port;
    }

    pub fn get_plugin_id(&self) -> &str {
        &self.plugin_id
    }

    pub fn set_plugin_id(&mut self, plugin_id: String) {
        self.plugin_id = plugin_id;
    }

    pub fn get_plugin_name(&self) -> &str {
        &self.plugin_name
    }

    pub fn set_plugin_name(&mut self, plugin_name: String) {
        self.plugin_name = plugin_name;
    }

    pub fn get_plugin_version(&self) -> &str {
        &self.plugin_version
    }

    pub fn set_plugin_version(&mut self, plugin_version: String) {
        self.plugin_version = plugin_version;
    }

    pub fn get_plugin_type(&self) -> &str {
        &self.plugin_type
    }

    pub fn set_plugin_type(&mut self, plugin_type: String) {
        self.plugin_type = plugin_type;
    }

    pub fn get_additional_config(&self) -> &HashMap<String, String> {
        &self.additional_config
    }

    pub fn set_additional_config(&mut self, additional_config: HashMap<String, String>) {
        self.additional_config = additional_config;
    }

    pub fn add_config(&mut self, key: String, value: String) {
        self.additional_config.insert(key, value);
    }

    pub fn get_config(&self, key: &str) -> Option<&String> {
        self.additional_config.get(key)
    }
}