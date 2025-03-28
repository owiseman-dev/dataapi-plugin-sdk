#ifndef PLUGIN_SDK_H
#define PLUGIN_SDK_H

#include <string>
#include <map>
#include "plugin_config.h"
#include "plugin_info.h"
#include "command_result.h"

/**
 * 插件SDK接口定义
 * 其他语言实现插件时可以参考此接口
 */
class PluginSDK {
public:
    virtual ~PluginSDK() {}
    
    /**
     * 初始化插件
     * @param config 插件配置
     * @return 是否初始化成功
     */
    virtual bool initialize(const PluginConfig& config) = 0;
    
    /**
     * 启动插件
     * @return 是否启动成功
     */
    virtual bool start() = 0;
    
    /**
     * 停止插件
     * @return 是否停止成功
     */
    virtual bool stop() = 0;
    
    /**
     * 获取插件信息
     * @return 插件信息
     */
    virtual PluginInfo getInfo() const = 0;
    
    /**
     * 执行插件命令
     * @param command 命令
     * @param params 参数
     * @return 命令执行结果
     */
    virtual CommandResult executeCommand(const std::string& command, const std::map<std::string, std::string>& params) = 0;
    
    /**
     * 处理来自主应用的消息
     * @param message 消息内容
     * @return 处理结果
     */
    virtual std::string handleMessage(const std::string& message) = 0;
};

#endif // PLUGIN_SDK_H