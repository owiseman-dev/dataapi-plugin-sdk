package com.owiseman.dataapi.plugins.sdk;

/**
 * 命令执行结果类
 */
public class CommandResult {
    private boolean success;
    private String result;
    private String errorMessage;

    public CommandResult(boolean success, String result) {
        this.success = success;
        this.result = result;
    }

    public CommandResult(boolean success, String result, String errorMessage) {
        this.success = success;
        this.result = result;
        this.errorMessage = errorMessage;
    }

    public static CommandResult success(String result) {
        return new CommandResult(true, result);
    }

    public static CommandResult error(String errorMessage) {
        return new CommandResult(false, null, errorMessage);
    }

    public boolean isSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }

    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }

    public String getErrorMessage() {
        return errorMessage;
    }

    public void setErrorMessage(String errorMessage) {
        this.errorMessage = errorMessage;
    }
}