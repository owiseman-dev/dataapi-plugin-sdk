use async_trait::async_trait;
use std::collections::HashMap;

use crate::command_result::CommandResult;
use crate::plugin_config::PluginConfig;
use crate::plugin_info::PluginInfo;

/// 插件SDK trait定义
/// 其他语言实现插件时可以参考此接口
#[async_trait]
pub trait PluginSDK {
    /// 初始化插件
    /// 
    /// # Arguments
    /// 
    /// * `config` - 插件配置
    /// 
    /// # Returns
    /// 
    /// 是否初始化成功
    async fn initialize(&mut self, config: PluginConfig) -> bool;

    /// 启动插件
    /// 
    /// # Returns
    /// 
    /// 是否启动成功
    async fn start(&mut self) -> bool;

    /// 停止插件
    /// 
    /// # Returns
    /// 
    /// 是否停止成功
    async fn stop(&mut self) -> bool;

    /// 获取插件信息
    /// 
    /// # Returns
    /// 
    /// 插件信息
    fn get_info(&self) -> PluginInfo;

    /// 执行插件命令
    /// 
    /// # Arguments
    /// 
    /// * `command` - 命令
    /// * `params` - 参数
    /// 
    /// # Returns
    /// 
    /// 命令执行结果
    async fn execute_command(&self, command: &str, params: &HashMap<String, String>) -> CommandResult;

    /// 处理来自主应用的消息
    /// 
    /// # Arguments
    /// 
    /// * `message` - 消息内容
    /// 
    /// # Returns
    /// 
    /// 处理结果
    async fn handle_message(&self, message: &str) -> String;
}