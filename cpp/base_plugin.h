#ifndef BASE_PLUGIN_H
#define BASE_PLUGIN_H

#include <thread>
#include <atomic>
#include <memory>
#include "plugin_sdk.h"
#include "plugin_config.h"
#include "plugin_info.h"

// 前向声明
namespace grpc {
    class Channel;
}

namespace plugin {
    class PluginServiceStub;
}

/**
 * 基础插件实现类
 */
class BasePlugin : public PluginSDK {
protected:
    PluginConfig config;
    PluginInfo info;
    std::shared_ptr<grpc::Channel> channel;
    std::unique_ptr<plugin::PluginServiceStub> stub;
    std::atomic<bool> running;
    std::thread heartbeatThread;
    
    void heartbeatLoop();

public:
    BasePlugin();
    virtual ~BasePlugin();
    
    bool initialize(const PluginConfig& config) override;
    bool start() override;
    bool stop() override;
    PluginInfo getInfo() const override;
    CommandResult executeCommand(const std::string& command, const std::map<std::string, std::string>& params) override;
    std::string handleMessage(const std::string& message) override;
};

#endif // BASE_PLUGIN_H