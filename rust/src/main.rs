use dataapi_plugin_sdk::{ExamplePlugin, PluginConfig, PluginSDK};
use std::error::Error;
use tokio::signal;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // 创建插件配置
    let mut config = PluginConfig::new();
    config.set_server_host("localhost".to_string());
    config.set_server_port(50051);
    config.set_plugin_name("示例插件".to_string());
    config.set_plugin_version("1.0.0".to_string());
    config.set_plugin_type("example".to_string());
    
    // 添加额外配置
    config.add_config("plugin.host".to_string(), "localhost".to_string());
    config.add_config("plugin.port".to_string(), "50052".to_string());
    
    // 创建插件实例
    let mut plugin = ExamplePlugin::new();
    
    // 初始化插件
    if !plugin.initialize(config).await {
        eprintln!("插件初始化失败");
        return Ok(());
    }
    
    // 启动插件
    if !plugin.start().await {
        eprintln!("插件启动失败");
        return Ok(());
    }
    
    println!("插件已启动，按 Ctrl+C 停止...");
    
    // 等待中断信号
    signal::ctrl_c().await?;
    
    // 停止插件
    plugin.stop().await;
    println!("插件已停止");
    
    Ok(())
}