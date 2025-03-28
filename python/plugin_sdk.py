from abc import ABC, abstractmethod
from .plugin_config import PluginConfig
from .plugin_info import PluginInfo
from .command_result import CommandResult

class PluginSDK(ABC):
    """
    插件SDK接口定义
    其他语言实现插件时可以参考此接口
    """
    
    @abstractmethod
    def initialize(self, config):
        """
        初始化插件
        :param config: 插件配置
        :return: 是否初始化成功
        """
        pass
    
    @abstractmethod
    def start(self):
        """
        启动插件
        :return: 是否启动成功
        """
        pass
    
    @abstractmethod
    def stop(self):
        """
        停止插件
        :return: 是否停止成功
        """
        pass
    
    @abstractmethod
    def get_info(self):
        """
        获取插件信息
        :return: 插件信息
        """
        pass
    
    @abstractmethod
    def execute_command(self, command, params):
        """
        执行插件命令
        :param command: 命令
        :param params: 参数
        :return: 命令执行结果
        """
        pass
    
    @abstractmethod
    def handle_message(self, message):
        """
        处理来自主应用的消息
        :param message: 消息内容
        :return: 处理结果
        """
        pass