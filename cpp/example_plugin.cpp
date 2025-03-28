#include "example_plugin.h"

ExamplePlugin::ExamplePlugin() : BasePlugin() {
}

bool ExamplePlugin::initialize(const PluginConfig& config) {
    bool result = BasePlugin::initialize(config);
    
    // 设置插件描述
    info.setDescription("这是一个示例插件");
    
    // 添加支持的命令
    info.addSupportedCommand("hello");
    info.addSupportedCommand("echo");
    
    // 添加支持的事件
    info.addSupportedEvent("startup");
    
    return result;
}

CommandResult ExamplePlugin::executeCommand(const std::string& command, const std::map<std::string, std::string>& params) {
    if (command == "hello") {
        return CommandResult(true, "Hello, World!", "");
    } else if (command == "echo") {
        auto it = params.find("message");
        std::string message = (it != params.end()) ? it->second : "";
        return CommandResult(true, "Echo: " + message, "");
    } else {
        return CommandResult(false, "", "未知命令: " + command);
    }
}

std::string ExamplePlugin::handleMessage(const std::string& message) {
    return "已收到消息: " + message;
}