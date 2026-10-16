import logging

from sqlalchemy.exc import SQLAlchemyError

from wxcloudrun import db
from wxcloudrun.model import Counters

# 初始化日志
logger = logging.getLogger('log')


def query_counterbyid(id):
    """
    根据ID查询Counter实体
    :param id: Counter的ID
    :return: Counter实体
    """
    try:
        return Counters.query.filter(Counters.id == id).first()
    except SQLAlchemyError as e:
        logger.error("query_counterbyid errorMsg= {} ".format(e))
        return None


def delete_counterbyid(id):
    """
    根据ID删除Counter实体
    :param id: Counter的ID
    """
    try:
        counter = Counters.query.get(id)
        if counter is None:
            return
        db.session.delete(counter)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error("delete_counterbyid errorMsg= {} ".format(e))


def insert_counter(counter):
    """
    插入一个Counter实体
    :param counter: Counters实体
    """
    try:
        db.session.add(counter)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error("insert_counter errorMsg= {} ".format(e))


def update_counterbyid(counter):
    """
    提交对counter实体的修改
    :param counter: Counters实体
    """
    try:
        db.session.add(counter)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error("update_counterbyid errorMsg= {} ".format(e))


def increase_counterbyid(id):
    """
    在数据库层面原子地将计数加1，避免并发请求时计数丢失
    :param id: Counter的ID
    :return: 加1后的Counter实体；记录不存在或出错时返回None
    """
    try:
        updated = Counters.query.filter(Counters.id == id).update(
            {Counters.count: Counters.count + 1}, synchronize_session=False)
        db.session.commit()
        if updated == 0:
            return None
        return query_counterbyid(id)
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error("increase_counterbyid errorMsg= {} ".format(e))
        return None
