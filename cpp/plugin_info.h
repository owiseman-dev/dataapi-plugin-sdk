#ifndef PLUGIN_INFO_H
#define PLUGIN_INFO_H

#include <string>
#include <vector>

/**
 * 插件信息类
 */
class PluginInfo {
private:
    std::string id;
    std::string name;
    std::string version;
    std::string type;
    std::string description;
    std::string status;
    std::vector<std::string> supportedCommands;
    std::vector<std::string> supportedEvents;

public:
    PluginInfo();
    
    std::string getId() const;
    void setId(const std::string& id);
    
    std::string getName() const;
    void setName(const std::string& name);
    
    std::string getVersion() const;
    void setVersion(const std::string& version);
    
    std::string getType() const;
    void setType(const std::string& type);
    
    std::string getDescription() const;
    void setDescription(const std::string& description);
    
    std::string getStatus() const;
    void setStatus(const std::string& status);
    
    const std::vector<std::string>& getSupportedCommands() const;
    void setSupportedCommands(const std::vector<std::string>& supportedCommands);
    void addSupportedCommand(const std::string& command);
    
    const std::vector<std::string>& getSupportedEvents() const;
    void setSupportedEvents(const std::vector<std::string>& supportedEvents);
    void addSupportedEvent(const std::string& event);
};

#endif // PLUGIN_INFO_H