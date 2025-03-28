use async_trait::async_trait;
use std::collections::HashMap;
use std::sync::{Arc, Mutex};
use std::time::Duration;
use tokio::sync::mpsc;
use tokio::task::JoinHandle;
use tonic::transport::{Channel, Endpoint};

use crate::command_result::CommandResult;
use crate::plugin_config::PluginConfig;
use crate::plugin_info::PluginInfo;
use crate::plugin_sdk::PluginSDK;

// 导入生成的protobuf代码
pub mod plugin {
    tonic::include_proto!("plugin");
}

use plugin::plugin_service_client::PluginServiceClient;
use plugin::{
    CommandRequest, HeartbeatRequest, PluginRegistration, StatusRequest, StopRequest,
};

/// 基础插件实现
pub struct BasePlugin {
    config: Option<PluginConfig>,
    info: PluginInfo,
    running: Arc<Mutex<bool>>,
    heartbeat_handle: Option<JoinHandle<()>>,
    shutdown_tx: Option<mpsc::Sender<()>>,
}

impl BasePlugin {
    pub fn new() -> Self {
        Self {
            config: None,
            info: PluginInfo::new(),
            running: Arc::new(Mutex::new(false)),
            heartbeat_handle: None,
            shutdown_tx: None,
        }
    }

    async fn create_client(&self) -> Result<PluginServiceClient<Channel>, Box<dyn std::error::Error>> {
        let config = self.config.as_ref().ok_or("Plugin not initialized")?;
        let endpoint = format!("http://{}:{}", config.get_server_host(), config.get_server_port());
        let channel = Endpoint::from_shared(endpoint)?.connect().await?;
        Ok(PluginServiceClient::new(channel))
    }

    async fn heartbeat_loop(
        plugin_id: String,
        status: String,
        running: Arc<Mutex<bool>>,
        mut shutdown_rx: mpsc::Receiver<()>,
        server_host: String,
        server_port: i32,
    ) {
        let endpoint = format!("http://{}:{}", server_host, server_port);
        
        loop {
            tokio::select! {
                _ = tokio::time::sleep(Duration::from_secs(5)) => {
                    let is_running = {
                        let guard = running.lock().unwrap();
                        *guard
                    };

                    if !is_running {
                        break;
                    }

                    match Endpoint::from_shared(endpoint.clone())
                        .and_then(|endpoint| Ok(endpoint.connect_lazy()))
                    {
                        Ok(channel) => {
                            let mut client = PluginServiceClient::new(channel);
                            let request = tonic::Request::new(HeartbeatRequest {
                                plugin_id: plugin_id.clone(),
                                status_info: status.clone(),
                            });

                            match client.heartbeat(request).await {
                                Ok(_) => {
                                    // 心跳成功
                                }
                                Err(e) => {
                                    eprintln!("心跳发送失败: {}", e);
                                }
                            }
                        }
                        Err(e) => {
                            eprintln!("创建gRPC客户端失败: {}", e);
                        }
                    }
                }
                _ = shutdown_rx.recv() => {
                    break;
                }
            }
        }
    }
}

#[async_trait]
impl PluginSDK for BasePlugin {
    async fn initialize(&mut self, config: PluginConfig) -> bool {
        self.config = Some(config.clone());
        
        // 设置插件基本信息
        self.info.set_id(config.get_plugin_id().to_string());
        self.info.set_name(config.get_plugin_name().to_string());
        self.info.set_version(config.get_plugin_version().to_string());
        self.info.set_type(config.get_plugin_type().to_string());
        
        true
    }

    async fn start(&mut self) -> bool {
        let is_running = {
            let mut guard = self.running.lock().unwrap();
            if *guard {
                return true;
            }
            *guard = true;
            true
        };

        if !is_running {
            return false;
        }

        let config = match &self.config {
            Some(config) => config,
            None => return false,
        };

        // 创建gRPC客户端
        let mut client = match self.create_client().await {
            Ok(client) => client,
            Err(e) => {
                eprintln!("创建gRPC客户端失败: {}", e);
                return false;
            }
        };

        // 注册插件
        let plugin_host = match config.get_config("plugin.host") {
            Some(host) => host.clone(),
            None => "localhost".to_string(),
        };

        let plugin_port = match config.get_config("plugin.port") {
            Some(port) => port.parse::<i32>().unwrap_or(50052),
            None => 50052,
        };

        let request = tonic::Request::new(PluginRegistration {
            name: self.info.get_name().to_string(),
            version: self.info.get_version().to_string(),
            r#type: self.info.get_type().to_string(),
            description: self.info.get_description().to_string(),
            host: plugin_host,
            port: plugin_port,
        });

        let response = match client.register_plugin(request).await {
            Ok(response) => response.into_inner(),
            Err(e) => {
                eprintln!("插件注册失败: {}", e);
                return false;
            }
        };

        if !response.success {
            eprintln!("插件注册失败: {}", response.message);
            return false;
        }

        // 设置插件ID
        self.info.set_id(response.plugin_id.clone());
        if let Some(config) = &mut self.config {
            config.set_plugin_id(response.plugin_id.clone());
        }

        // 启动心跳线程
        let (shutdown_tx, shutdown_rx) = mpsc::channel(1);
        self.shutdown_tx = Some(shutdown_tx);

        let plugin_id = self.info.get_id().to_string();
        let status = self.info.get_status().to_string();
        let running = Arc::clone(&self.running);
        let server_host = config.get_server_host().to_string();
        let server_port = config.get_server_port();

        let handle = tokio::spawn(async move {
            Self::heartbeat_loop(
                plugin_id,
                status,
                running,
                shutdown_rx,
                server_host,
                server_port,
            )
            .await;
        });

        self.heartbeat_handle = Some(handle);

        true
    }

    async fn stop(&mut self) -> bool {
        let was_running = {
            let mut guard = self.running.lock().unwrap();
            let was_running = *guard;
            *guard = false;
            was_running
        };

        if !was_running {
            return true;
        }

        // 停止心跳线程
        if let Some(tx) = &self.shutdown_tx {
            let _ = tx.send(()).await;
        }

        if let Some(handle) = self.heartbeat_handle.take() {
            let _ = handle.await;
        }

        // 通知服务器停止插件
        if let Some(client_result) = self.create_client().await.ok() {
            let mut client = client_result;
            let request = tonic::Request::new(StopRequest {
                plugin_id: self.info.get_id().to_string(),
            });

            let _ = client.stop_plugin(request).await;
        }

        true
    }

    fn get_info(&self) -> PluginInfo {
        self.info.clone()
    }

    async fn execute_command(&self, command: &str, params: &HashMap<String, String>) -> CommandResult {
        // 子类应该重写此方法
        CommandResult::new(
            false,
            String::new(),
            format!("未实现的命令: {}", command),
        )
    }

    async fn handle_message(&self, message: &str) -> String {
        // 子类应该重写此方法
        format!("未处理的消息: {}", message)
    }
}