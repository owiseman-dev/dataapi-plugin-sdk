#include "plugin_config.h"

PluginConfig::PluginConfig() : serverPort(0) {
}

std::string PluginConfig::getServerHost() const {
    return serverHost;
}

void PluginConfig::setServerHost(const std::string& serverHost) {
    this->serverHost = serverHost;
}

int PluginConfig::getServerPort() const {
    return serverPort;
}

void PluginConfig::setServerPort(int serverPort) {
    this->serverPort = serverPort;
}

std::string PluginConfig::getPluginId() const {
    return pluginId;
}

void PluginConfig::setPluginId(const std::string& pluginId) {
    this->pluginId = pluginId;
}

std::string PluginConfig::getPluginName() const {
    return pluginName;
}

void PluginConfig::setPluginName(const std::string& pluginName) {
    this->pluginName = pluginName;
}

std::string PluginConfig::getPluginVersion() const {
    return pluginVersion;
}

void PluginConfig::setPluginVersion(const std::string& pluginVersion) {
    this->pluginVersion = pluginVersion;
}

std::string PluginConfig::getPluginType() const {
    return pluginType;
}

void PluginConfig::setPluginType(const std::string& pluginType) {
    this->pluginType = pluginType;
}

const std::map<std::string, std::string>& PluginConfig::getAdditionalConfig() const {
    return additionalConfig;
}

void PluginConfig::setAdditionalConfig(const std::map<std::string, std::string>& additionalConfig) {
    this->additionalConfig = additionalConfig;
}

void PluginConfig::addConfig(const std::string& key, const std::string& value) {
    this->additionalConfig[key] = value;
}

std::string PluginConfig::getConfig(const std::string& key) const {
    auto it = additionalConfig.find(key);
    if (it != additionalConfig.end()) {
        return it->second;
    }
    return "";
}