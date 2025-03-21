package com.owiseman.dataapi.plugins.sdk;

import java.util.Map;

/**
 * 插件SDK接口定义
 * 其他语言实现插件时可以参考此接口
 */
public interface PluginSDK {

    /**
     * 初始化插件
     * @param config 插件配置
     * @return 是否初始化成功
     */
    boolean initialize(PluginConfig config);

    /**
     * 启动插件
     * @return 是否启动成功
     */
    boolean start();

    /**
     * 停止插件
     * @return 是否停止成功
     */
    boolean stop();

    /**
     * 获取插件信息
     * @return 插件信息
     */
    PluginInfo getInfo();

    /**
     * 执行插件命令
     * @param command 命令
     * @param params 参数
     * @return 命令执行结果
     */
    CommandResult executeCommand(String command, Map<String, String> params);

    /**
     * 处理来自主应用的消息
     * @param message 消息内容
     * @return 处理结果
     */
    String handleMessage(String message);
}