use async_trait::async_trait;
use std::collections::HashMap;

use crate::base_plugin::BasePlugin;
use crate::command_result::CommandResult;
use crate::plugin_config::PluginConfig;
use crate::plugin_sdk::PluginSDK;

/// 示例插件实现
pub struct ExamplePlugin {
    base: BasePlugin,
}

impl ExamplePlugin {
    pub fn new() -> Self {
        Self {
            base: BasePlugin::new(),
        }
    }
}

#[async_trait]
impl PluginSDK for ExamplePlugin {
    async fn initialize(&mut self, config: PluginConfig) -> bool {
        let result = self.base.initialize(config).await;
        
        // 设置插件描述
        let mut info = self.base.get_info();
        info.set_description("这是一个示例插件".to_string());
        
        // 添加支持的命令
        info.add_supported_command("hello".to_string());
        info.add_supported_command("echo".to_string());
        
        // 添加支持的事件
        info.add_supported_event("startup".to_string());
        
        result
    }

    async fn start(&mut self) -> bool {
        self.base.start().await
    }

    async fn stop(&mut self) -> bool {
        self.base.stop().await
    }

    fn get_info(&self) -> crate::plugin_info::PluginInfo {
        self.base.get_info()
    }

    async fn execute_command(&self, command: &str, params: &HashMap<String, String>) -> CommandResult {
        match command {
            "hello" => CommandResult::new(
                true,
                "Hello, World!".to_string(),
                String::new(),
            ),
            "echo" => {
                let message = params.get("message").cloned().unwrap_or_default();
                CommandResult::new(
                    true,
                    format!("Echo: {}", message),
                    String::new(),
                )
            }
            _ => CommandResult::new(
                false,
                String::new(),
                format!("未知命令: {}", command),
            ),
        }
    }

    async fn handle_message(&self, message: &str) -> String {
        format!("已收到消息: {}", message)
    }
}