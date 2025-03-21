package com.owiseman.dataapi.plugins.sdk;

import java.util.HashMap;
import java.util.Map;

/**
 * 插件配置类
 */
public class PluginConfig {
    private String serverHost;
    private int serverPort;
    private String pluginId;
    private String pluginName;
    private String pluginVersion;
    private String pluginType;
    private Map<String, String> additionalConfig = new HashMap<>();

    public String getServerHost() {
        return serverHost;
    }

    public void setServerHost(String serverHost) {
        this.serverHost = serverHost;
    }

    public int getServerPort() {
        return serverPort;
    }

    public void setServerPort(int serverPort) {
        this.serverPort = serverPort;
    }

    public String getPluginId() {
        return pluginId;
    }

    public void setPluginId(String pluginId) {
        this.pluginId = pluginId;
    }

    public String getPluginName() {
        return pluginName;
    }

    public void setPluginName(String pluginName) {
        this.pluginName = pluginName;
    }

    public String getPluginVersion() {
        return pluginVersion;
    }

    public void setPluginVersion(String pluginVersion) {
        this.pluginVersion = pluginVersion;
    }

    public String getPluginType() {
        return pluginType;
    }

    public void setPluginType(String pluginType) {
        this.pluginType = pluginType;
    }

    public Map<String, String> getAdditionalConfig() {
        return additionalConfig;
    }

    public void setAdditionalConfig(Map<String, String> additionalConfig) {
        this.additionalConfig = additionalConfig;
    }

    public void addConfig(String key, String value) {
        this.additionalConfig.put(key, value);
    }

    public String getConfig(String key) {
        return this.additionalConfig.get(key);
    }
}