#include <iostream>
#include <csignal>
#include "example_plugin.h"

// 全局插件实例
std::unique_ptr<ExamplePlugin> plugin;

// 信号处理函数
void signalHandler(int signal) {
    std::cout << "接收到信号: " << signal << ", 正在停止插件..." << std::endl;
    if (plugin) {
        plugin->stop();
    }
    exit(0);
}

int main() {
    // 注册信号处理
    std::signal(SIGINT, signalHandler);
    std::signal(SIGTERM, signalHandler);
    
    // 创建插件配置
    PluginConfig config;
    config.setServerHost("localhost");
    config.setServerPort(50051);
    config.setPluginName("示例插件");
    config.setPluginVersion("1.0.0");
    config.setPluginType("example");
    
    // 添加额外配置
    config.addConfig("plugin.host", "localhost");
    config.addConfig("plugin.port", "50052");
    
    // 创建插件实例
    plugin = std::make_unique<ExamplePlugin>();
    
    // 初始化插件
    if (!plugin->initialize(config)) {
        std::cerr << "插件初始化失败" << std::endl;
        return 1;
    }
    
    // 启动插件
    if (!plugin->start()) {
        std::cerr << "插件启动失败" << std::endl;
        return 1;
    }
    
    std::cout << "插件已启动，按 Ctrl+C 停止..." << std::endl;
    
    // 保持主线程运行
    while (true) {
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    
    return 0;
}