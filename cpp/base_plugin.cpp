#include "base_plugin.h"
#include <chrono>
#include <iostream>
#include <grpcpp/grpcpp.h>
#include "plugin_service.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;
using plugin::PluginService;
using plugin::PluginRegistration;
using plugin::RegistrationResponse;
using plugin::HeartbeatRequest;
using plugin::HeartbeatResponse;
using plugin::StatusRequest;
using plugin::StatusResponse;
using plugin::CommandRequest;
using plugin::CommandResponse;
using plugin::StopRequest;
using plugin::StopResponse;

BasePlugin::BasePlugin() : running(false) {
}

BasePlugin::~BasePlugin() {
    stop();
}

bool BasePlugin::initialize(const PluginConfig& config) {
    this->config = config;
    
    // 设置插件基本信息
    info.setId(config.getPluginId());
    info.setName(config.getPluginName());
    info.setVersion(config.getPluginVersion());
    info.setType(config.getPluginType());
    
    return true;
}

bool BasePlugin::start() {
    if (running) {
        return true;
    }
    
    // 创建 gRPC 通道
    std::string serverAddress = config.getServerHost() + ":" + std::to_string(config.getServerPort());
    channel = grpc::CreateChannel(serverAddress, grpc::InsecureChannelCredentials());
    stub = PluginService::NewStub(channel);
    
    // 注册插件
    PluginRegistration request;
    request.set_name(info.getName());
    request.set_version(info.getVersion());
    request.set_type(info.getType());
    request.set_description(info.getDescription());
    request.set_host(config.getConfig("plugin.host"));
    request.set_port(std::stoi(config.getConfig("plugin.port")));
    
    RegistrationResponse response;
    ClientContext context;
    Status status = stub->RegisterPlugin(&context, request, &response);
    
    if (!status.ok() || !response.success()) {
        std::cerr << "插件注册失败: " << response.message() << std::endl;
        return false;
    }
    
    // 设置插件ID
    info.setId(response.plugin_id());
    
    // 启动心跳线程
    running = true;
    heartbeatThread = std::thread(&BasePlugin::heartbeatLoop, this);
    
    return true;
}

bool BasePlugin::stop() {
    if (!running) {
        return true;
    }
    
    running = false;
    
    if (heartbeatThread.joinable()) {
        heartbeatThread.join();
    }
    
    if (stub) {
        StopRequest request;
        request.set_plugin_id(info.getId());
        
        StopResponse response;
        ClientContext context;
        Status status = stub->StopPlugin(&context, request, &response);
    }
    
    return true;
}

PluginInfo BasePlugin::getInfo() const {
    return info;
}

CommandResult BasePlugin::executeCommand(const std::string& command, const std::map<std::string, std::string>& params) {
    // 子类应该重写此方法
    return CommandResult(false, "", "未实现的命令");
}

std::string BasePlugin::handleMessage(const std::string& message) {
    // 子类应该重写此方法
    return "未处理的消息";
}

void BasePlugin::heartbeatLoop() {
    while (running) {
        try {
            HeartbeatRequest request;
            request.set_plugin_id(info.getId());
            request.set_status_info(info.getStatus().empty() ? "RUNNING" : info.getStatus());
            
            HeartbeatResponse response;
            ClientContext context;
            Status status = stub->Heartbeat(&context, request, &response);
            
            if (!status.ok()) {
                std::cerr << "心跳发送失败: " << status.error_message() << std::endl;
            }
        } catch (const std::exception& e) {
            std::cerr << "心跳发送异常: " << e.what() << std::endl;
        }
        
        // 每5秒发送一次心跳
        std::this_thread::sleep_for(std::chrono::seconds(5));
    }
}