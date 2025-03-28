#include "command_result.h"

CommandResult::CommandResult(bool success, const std::string& result, const std::string& errorMessage)
    : success(success), result(result), errorMessage(errorMessage) {
}

bool CommandResult::isSuccess() const {
    return success;
}

void CommandResult::setSuccess(bool success) {
    this->success = success;
}

std::string CommandResult::getResult() const {
    return result;
}

void CommandResult::setResult(const std::string& result) {
    this->result = result;
}

std::string CommandResult::getErrorMessage() const {
    return errorMessage;
}

void CommandResult::setErrorMessage(const std::string& errorMessage) {
    this->errorMessage = errorMessage;
}