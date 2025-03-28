cmake_minimum_required(VERSION 3.10)
project(dataapi-plugin-sdk)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 查找 gRPC 和 Protobuf 包
find_package(gRPC CONFIG REQUIRED)
find_package(Protobuf CONFIG REQUIRED)

# 添加生成的 protobuf 文件目录
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../target/generated-sources/protobuf/cpp)

# 添加源文件
set(SOURCES
    plugin_config.cpp
    plugin_info.cpp
    command_result.cpp
    base_plugin.cpp
    example_plugin.cpp
)

# 添加头文件
set(HEADERS
    plugin_config.h
    plugin_info.h
    command_result.h
    plugin_sdk.h
    base_plugin.h
    example_plugin.h
)

# 添加库
add_library(${PROJECT_NAME} STATIC ${SOURCES} ${HEADERS})

# 链接 gRPC 和 Protobuf 库
target_link_libraries(${PROJECT_NAME}
    gRPC::grpc++
    protobuf::libprotobuf
)

# 添加示例可执行文件
add_executable(example_plugin_app example_main.cpp)
target_link_libraries(example_plugin_app ${PROJECT_NAME})