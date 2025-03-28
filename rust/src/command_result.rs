/// 命令执行结果结构体
#[derive(Debug, Clone)]
pub struct CommandResult {
    success: bool,
    result: String,
    error_message: String,
}

impl CommandResult {
    pub fn new(success: bool, result: String, error_message: String) -> Self {
        Self {
            success,
            result,
            error_message,
        }
    }

    pub fn is_success(&self) -> bool {
        self.success
    }

    pub fn set_success(&mut self, success: bool) {
        self.success = success;
    }

    pub fn get_result(&self) -> &str {
        &self.result
    }

    pub fn set_result(&mut self, result: String) {
        self.result = result;
    }

    pub fn get_error_message(&self) -> &str {
        &self.error_message
    }

    pub fn set_error_message(&mut self, error_message: String) {
        self.error_message = error_message;
    }
}