from .plugin_config import PluginConfig
from .example_plugin import ExamplePlugin

def main():
    # 创建插件配置
    config = PluginConfig()
    config.set_server_host("localhost")
    config.set_server_port(50051)
    config.set_plugin_name("示例插件")
    config.set_plugin_version("1.0.0")
    config.set_plugin_type("example")
    
    # 添加额外配置
    config.add_config("plugin.host", "localhost")
    config.add_config("plugin.port", "50052")
    
    # 创建插件实例
    plugin = ExamplePlugin()
    
    # 初始化插件
    if not plugin.initialize(config):
        print("插件初始化失败")
        return
    
    # 启动插件
    if not plugin.start():
        print("插件启动失败")
        return
    
    print("插件已启动，按 Ctrl+C 停止...")
    
    try:
        # 保持主线程运行
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # 停止插件
        plugin.stop()
        print("插件已停止")

if __name__ == "__main__":
    main()