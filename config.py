import os

# 是否开启debug模式（生产环境请保持关闭，本地调试可设置环境变量 DEBUG=true）
DEBUG = os.environ.get("DEBUG", "false").lower() in ("1", "true", "yes")

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", 'root')
password = os.environ.get("MYSQL_PASSWORD", 'root')
db_address = os.environ.get("MYSQL_ADDRESS", '127.0.0.1:3306')
