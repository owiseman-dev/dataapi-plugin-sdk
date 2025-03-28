#ifndef COMMAND_RESULT_H
#define COMMAND_RESULT_H

#include <string>

/**
 * 命令执行结果类
 */
class CommandResult {
private:
    bool success;
    std::string result;
    std::string errorMessage;

public:
    CommandResult(bool success = false, const std::string& result = "", const std::string& errorMessage = "");
    
    bool isSuccess() const;
    void setSuccess(bool success);
    
    std::string getResult() const;
    void setResult(const std::string& result);
    
    std::string getErrorMessage() const;
    void setErrorMessage(const std::string& errorMessage);
};

#endif // COMMAND_RESULT_H