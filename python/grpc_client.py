import grpc
from .plugin_service_pb2 import (
    PluginRegistration, HeartbeatRequest, StatusRequest,
    CommandRequest, StopRequest
)
from .plugin_service_pb2_grpc import PluginServiceStub

class GrpcClient:
    """gRPC 客户端工具类"""
    
    def __init__(self, host, port):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = PluginServiceStub(self.channel)
        
    def register_plugin(self, name, version, type, description, host, port):
        """
        注册插件
        :return: 注册响应
        """
        request = PluginRegistration(
            name=name,
            version=version,
            type=type,
            description=description,
            host=host,
            port=port
        )
        return self.stub.RegisterPlugin(request)
    
    def send_heartbeat(self, plugin_id, status_info):
        """
        发送心跳
        :return: 心跳响应
        """
        request = HeartbeatRequest(
            plugin_id=plugin_id,
            status_info=status_info
        )
        return self.stub.Heartbeat(request)
    
    def get_status(self, plugin_id):
        """
        获取状态
        :return: 状态响应
        """
        request = StatusRequest(plugin_id=plugin_id)
        return self.stub.GetStatus(request)
    
    def execute_command(self, plugin_id, command, parameters):
        """
        执行命令
        :return: 命令响应
        """
        request = CommandRequest(
            plugin_id=plugin_id,
            command=command,
            parameters=parameters
        )
        return self.stub.ExecuteCommand(request)
    
    def stop_plugin(self, plugin_id):
        """
        停止插件
        :return: 停止响应
        """
        request = StopRequest(plugin_id=plugin_id)
        return self.stub.StopPlugin(request)
    
    def close(self):
        """关闭连接"""
        self.channel.close()