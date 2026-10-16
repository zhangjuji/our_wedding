from urllib.parse import quote_plus

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import config

# 因MySQLDB不支持Python3，使用pymysql扩展库代替MySQLDB库
pymysql.install_as_MySQLdb()

# 初始化web应用
app = Flask(__name__, instance_relative_config=True)

# 加载配置
app.config.from_object('config')

# 设定数据库链接（对用户名和密码做URL编码，避免密码中含 @ : / 等特殊字符时连接失败）
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/flask_demo'.format(
    quote_plus(config.username), quote_plus(config.password), config.db_address)
# 关闭对象修改追踪，减少内存开销并消除启动警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 连接池预检，避免MySQL空闲断开后出现 "MySQL server has gone away"
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_pre_ping': True, 'pool_recycle': 280}

# 初始化DB操作对象
db = SQLAlchemy(app)

# 加载控制器
from wxcloudrun import views  # noqa: E402,F401
