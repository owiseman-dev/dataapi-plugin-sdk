# DataAPI Plugin SDK - Rust 版本

这是 DataAPI Plugin SDK 的 Rust 实现版本，用于开发与 DataAPI 系统集成的 Rust 插件。

## 依赖项

- Rust 1.56.0 或更高版本
- Cargo
- Protobuf 编译器 (protoc)

## 安装依赖项

### 在 macOS 上安装依赖项

使用 Homebrew 安装 Rust 和 Protobuf：

```bash
# 安装 Homebrew（如果尚未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Rust 和 Protobuf
brew install rust protobuf

# 或者使用 rustup 安装 Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh