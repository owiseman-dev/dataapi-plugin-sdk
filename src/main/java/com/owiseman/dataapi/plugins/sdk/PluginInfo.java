package com.owiseman.dataapi.plugins.sdk;

import java.util.ArrayList;
import java.util.List;

/**
 * 插件信息类
 */
public class PluginInfo {
    private String id;
    private String name;
    private String version;
    private String type;
    private String description;
    private String status;
    private List<String> supportedCommands = new ArrayList<>();
    private List<String> supportedEvents = new ArrayList<>();

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public List<String> getSupportedCommands() {
        return supportedCommands;
    }

    public void setSupportedCommands(List<String> supportedCommands) {
        this.supportedCommands = supportedCommands;
    }

    public void addSupportedCommand(String command) {
        this.supportedCommands.add(command);
    }

    public List<String> getSupportedEvents() {
        return supportedEvents;
    }

    public void setSupportedEvents(List<String> supportedEvents) {
        this.supportedEvents = supportedEvents;
    }

    public void addSupportedEvent(String event) {
        this.supportedEvents.add(event);
    }
}