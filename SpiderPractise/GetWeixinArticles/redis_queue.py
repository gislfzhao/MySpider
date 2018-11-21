# -*- coding: utf-8 -*-
from .weixin_request import WeixinRequest
from pickle import dumps, loads
from redis import StrictRedis

REDIS_KEY = 'WeixinRequests'
REDIS_KEY_2 = 'WeixinReqs'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None


class RedisQueue:
    def __init__(self):
        """
        初始化RedisQueue类
        """
        self.db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD)

    def add(self, req):
        """
        向队列中添加序列化后的Request
        :param req: 请求对象
        :return: 添加结果
        """
        if isinstance(req, WeixinRequest):
            # self.db.rpush(REDIS_KEY_2, dumps(req))
            return self.db.rpush(REDIS_KEY, dumps(req))
        return False

    def pop(self):
        """
        取出下一个Request
        :return: Request or None
        """
        if self.db.llen(REDIS_KEY):
            return loads(self.db.lpop(REDIS_KEY))
        else:
            return False

    def empty(self):
        """
        判断队列是否为空
        :return: True or False
        """
        return self.db.llen(REDIS_KEY) == 0

    def delete(self):
        """
        清除键
        :return: None
        """
        self.db.delete(REDIS_KEY)
