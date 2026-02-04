#!/bin/zsh
# 简化版修复脚本

echo "🧹 1. 清理环境..."
pip uninstall -y mysqlclient
brew uninstall mysql-client --ignore-dependencies 2>/dev/null || true
brew uninstall mysql --ignore-dependencies 2>/dev/null || true
brew uninstall openssl@3 --ignore-dependencies 2>/dev/null || true

echo "📦 2. 安装依赖..."
# 确保使用 ARM 版 Homebrew
if [ -f /opt/homebrew/bin/brew ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

# 安装必需依赖
brew install mysql-client
brew install pkg-config

echo "⚙️ 3. 设置环境变量..."
# 获取实际路径
MYSQL_PREFIX=$(brew --prefix mysql-client)
OPENSSL_PREFIX=$(brew --prefix openssl@3 2>/dev/null || echo "/opt/homebrew/opt/openssl")

export PATH="${MYSQL_PREFIX}/bin:$PATH"
export LDFLAGS="-L${MYSQL_PREFIX}/lib"
export CPPFLAGS="-I${MYSQL_PREFIX}/include"
export PKG_CONFIG_PATH="${MYSQL_PREFIX}/lib/pkgconfig"

# 如果有 openssl
if [ -d "${OPENSSL_PREFIX}" ]; then
    export LDFLAGS="${LDFLAGS} -L${OPENSSL_PREFIX}/lib"
    export CPPFLAGS="${CPPFLAGS} -I${OPENSSL_PREFIX}/include"
    export PKG_CONFIG_PATH="${OPENSSL_PREFIX}/lib/pkgconfig:${PKG_CONFIG_PATH}"
fi

echo "🔧 4. 验证依赖..."
echo "mysql_config: $(which mysql_config)"
echo "pkg-config: $(which pkg-config)"
pkg-config --cflags mysqlclient 2>/dev/null && echo "✅ pkg-config 能找到 mysqlclient" || echo "❌ pkg-config 找不到 mysqlclient"

echo "🚀 5. 开始安装 mysqlclient..."
# 尝试多种安装方式
echo "方式1: 从源码编译..."
pip install --no-binary :all: mysqlclient 2>&1 | tail -50 || {
    echo "方式1失败，尝试方式2..."
    echo "方式2: 使用系统编译器标志..."
    env LDFLAGS="$LDFLAGS" CPPFLAGS="$CPPFLAGS" pip install mysqlclient 2>&1 | tail -50
}

echo "✅ 完成！"