class CommandResult:
    """命令执行结果类"""
    
    def __init__(self, success=False, result=None, error_message=None):
        self.success = success
        self.result = result
        self.error_message = error_message
        
    def is_success(self):
        return self.success
    
    def set_success(self, success):
        self.success = success
        
    def get_result(self):
        return self.result
    
    def set_result(self, result):
        self.result = result
        
    def get_error_message(self):
        return self.error_message
    
    def set_error_message(self, error_message):
        self.error_message = error_message