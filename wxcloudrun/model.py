from datetime import datetime

from wxcloudrun import db


# 计数表
class Counters(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Counters'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=1)
    # 注意：default 传入函数本身（datetime.now），而不是 datetime.now()，
    # 否则时间只会在程序启动时计算一次，之后所有记录都是同一个时间
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now)
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now,
                           onupdate=datetime.now)
