#include "plugin_info.h"

PluginInfo::PluginInfo() {
}

std::string PluginInfo::getId() const {
    return id;
}

void PluginInfo::setId(const std::string& id) {
    this->id = id;
}

std::string PluginInfo::getName() const {
    return name;
}

void PluginInfo::setName(const std::string& name) {
    this->name = name;
}

std::string PluginInfo::getVersion() const {
    return version;
}

void PluginInfo::setVersion(const std::string& version) {
    this->version = version;
}

std::string PluginInfo::getType() const {
    return type;
}

void PluginInfo::setType(const std::string& type) {
    this->type = type;
}

std::string PluginInfo::getDescription() const {
    return description;
}

void PluginInfo::setDescription(const std::string& description) {
    this->description = description;
}

std::string PluginInfo::getStatus() const {
    return status;
}

void PluginInfo::setStatus(const std::string& status) {
    this->status = status;
}

const std::vector<std::string>& PluginInfo::getSupportedCommands() const {
    return supportedCommands;
}

void PluginInfo::setSupportedCommands(const std::vector<std::string>& supportedCommands) {
    this->supportedCommands = supportedCommands;
}

void PluginInfo::addSupportedCommand(const std::string& command) {
    this->supportedCommands.push_back(command);
}

const std::vector<std::string>& PluginInfo::getSupportedEvents() const {
    return supportedEvents;
}

void PluginInfo::setSupportedEvents(const std::vector<std::string>& supportedEvents) {
    this->supportedEvents = supportedEvents;
}

void PluginInfo::addSupportedEvent(const std::string& event) {
    this->supportedEvents.push_back(event);
}