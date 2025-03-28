from .base_plugin import BasePlugin
from .command_result import CommandResult

class ExamplePlugin(BasePlugin):
    """示例插件实现"""
    
    def __init__(self):
        super().__init__()
        
    def initialize(self, config):
        """初始化插件"""
        result = super().initialize(config)
        
        # 设置插件描述
        self.info.set_description("这是一个示例插件")
        
        # 添加支持的命令
        self.info.add_supported_command("hello")
        self.info.add_supported_command("echo")
        
        # 添加支持的事件
        self.info.add_supported_event("startup")
        
        return result
    
    def execute_command(self, command, params):
        """执行插件命令"""
        if command == "hello":
            return CommandResult(True, "Hello, World!", None)
        elif command == "echo":
            message = params.get("message", "")
            return CommandResult(True, f"Echo: {message}", None)
        else:
            return CommandResult(False, None, f"未知命令: {command}")
    
    def handle_message(self, message):
        """处理消息"""
        return f"已收到消息: {message}"