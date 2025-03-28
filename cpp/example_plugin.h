#ifndef EXAMPLE_PLUGIN_H
#define EXAMPLE_PLUGIN_H

#include "base_plugin.h"

/**
 * 示例插件实现
 */
class ExamplePlugin : public BasePlugin {
public:
    ExamplePlugin();
    
    bool initialize(const PluginConfig& config) override;
    CommandResult executeCommand(const std::string& command, const std::map<std::string, std::string>& params) override;
    std::string handleMessage(const std::string& message) override;
};

#endif // EXAMPLE_PLUGIN_H