import threading
import time
from .plugin_sdk import PluginSDK
from .plugin_info import PluginInfo
from .command_result import CommandResult
from .grpc_client import GrpcClient

class BasePlugin(PluginSDK):
    """基础插件实现类"""
    
    def __init__(self):
        self.config = None
        self.info = PluginInfo()
        self.client = None
        self.running = False
        self.heartbeat_thread = None
        
    def initialize(self, config):
        """
        初始化插件
        :param config: 插件配置
        :return: 是否初始化成功
        """
        self.config = config
        
        # 设置插件基本信息
        self.info.set_id(config.get_plugin_id())
        self.info.set_name(config.get_plugin_name())
        self.info.set_version(config.get_plugin_version())
        self.info.set_type(config.get_plugin_type())
        
        # 创建 gRPC 客户端
        self.client = GrpcClient(config.get_server_host(), config.get_server_port())
        
        return True
    
    def start(self):
        """
        启动插件
        :return: 是否启动成功
        """
        if self.running:
            return True
            
        # 注册插件
        response = self.client.register_plugin(
            self.info.get_name(),
            self.info.get_version(),
            self.info.get_type(),
            self.info.get_description(),
            self.config.get_config("plugin.host"),
            int(self.config.get_config("plugin.port"))
        )
        
        if not response.success:
            print(f"插件注册失败: {response.message}")
            return False
            
        # 设置插件ID
        self.info.set_id(response.plugin_id)
        self.config.set_plugin_id(response.plugin_id)
        
        # 启动心跳线程
        self.running = True
        self.heartbeat_thread = threading.Thread(target=self._heartbeat_loop)
        self.heartbeat_thread.daemon = True
        self.heartbeat_thread.start()
        
        return True
    
    def stop(self):
        """
        停止插件
        :return: 是否停止成功
        """
        if not self.running:
            return True
            
        self.running = False
        
        if self.heartbeat_thread:
            self.heartbeat_thread.join(timeout=2.0)
            
        if self.client:
            self.client.stop_plugin(self.info.get_id())
            self.client.close()
            
        return True
    
    def get_info(self):
        """
        获取插件信息
        :return: 插件信息
        """
        return self.info
    
    def execute_command(self, command, params):
        """
        执行插件命令
        :param command: 命令
        :param params: 参数
        :return: 命令执行结果
        """
        # 子类应该重写此方法
        return CommandResult(False, None, "未实现的命令")
    
    def handle_message(self, message):
        """
        处理来自主应用的消息
        :param message: 消息内容
        :return: 处理结果
        """
        # 子类应该重写此方法
        return "未处理的消息"
    
    def _heartbeat_loop(self):
        """心跳循环"""
        while self.running:
            try:
                response = self.client.send_heartbeat(
                    self.info.get_id(),
                    self.info.get_status() or "RUNNING"
                )
                # 可以处理心跳响应
            except Exception as e:
                print(f"心跳发送失败: {str(e)}")
            
            # 每5秒发送一次心跳
            time.sleep(5)