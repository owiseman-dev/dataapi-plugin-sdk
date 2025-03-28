#ifndef PLUGIN_CONFIG_H
#define PLUGIN_CONFIG_H

#include <string>
#include <map>

/**
 * 插件配置类
 */
class PluginConfig {
private:
    std::string serverHost;
    int serverPort;
    std::string pluginId;
    std::string pluginName;
    std::string pluginVersion;
    std::string pluginType;
    std::map<std::string, std::string> additionalConfig;

public:
    PluginConfig();
    
    std::string getServerHost() const;
    void setServerHost(const std::string& serverHost);
    
    int getServerPort() const;
    void setServerPort(int serverPort);
    
    std::string getPluginId() const;
    void setPluginId(const std::string& pluginId);
    
    std::string getPluginName() const;
    void setPluginName(const std::string& pluginName);
    
    std::string getPluginVersion() const;
    void setPluginVersion(const std::string& pluginVersion);
    
    std::string getPluginType() const;
    void setPluginType(const std::string& pluginType);
    
    const std::map<std::string, std::string>& getAdditionalConfig() const;
    void setAdditionalConfig(const std::map<std::string, std::string>& additionalConfig);
    
    void addConfig(const std::string& key, const std::string& value);
    std::string getConfig(const std::string& key) const;
};

#endif // PLUGIN_CONFIG_H