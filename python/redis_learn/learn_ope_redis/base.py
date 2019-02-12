#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: base.py.py
@time: 2019/2/12 11:57
"""

import redis
import time

redis_conf = dict(
    host = "192.168.2.253",
    port = 6379,
    db = 0,
)

class RedisQueue(object):
    def __init__(self, name, namespace = "queue"):
        self._db = redis.StrictRedis(host=redis_conf['host'], port=redis_conf['port'], db = redis_conf['db'])
        self._key = name

    def pull(self, data):
        return self._db.lpush(self._key, data)

    def get(self):
        return self._db.lpop(self._key)

    def empty(self):
        return self._db.llen(self._key) == 0


class RedisConn(object):
    def __init__(self, conf):
        self.port = conf["port"]
        self.db = conf["db"]
        self.host = conf["host"]
        self.r = self.conn()

    def conn(self):
        return redis.StrictRedis(host = self.host, port = self.port, db = self.db)


def test_command():
    Redis= RedisConn(redis_conf)
    Redis.r.hset("hash1", "key1", "12")
    redis_ret = Redis.r.hget('hash1', 'key1')
    print redis_ret
    print Redis.r.hgetall("hash1")

def init_park_conf_to_redis():
    park_conf = dict(
        park_ip = "192.168.1.1",
        park_name = "测试车场",
        device_id = "1",
    )
    redis_n = RedisConn(redis_conf)
    for key, value in park_conf.items():
        # print key, value
        redis_n.r.hset("park_conf", key, value)

def init_device_conf_to_redis(redisobj):
    device_conf = dict(
        id = 1,
        park_in = "进口1",
        park_out = "进口2",
    )
    for key, value in device_conf.items():
        redisobj.hset("device_conf", key, value)

    print "init device_conf end"


def get_reids_conf(redisobj, key, field = None):
    if field:
        return redisobj.hget(key, field)
    else:
        return redisobj.hgetall(key)


if __name__ == "__main__":

    ''' 
    //test common operater
    redis = RedisConn(redis_conf)
    # test_command()alueError: too many values to unpack

    # init_device_conf_to_redis(redis.r)

    park_conf = get_reids_conf(redis.r, "park_conf")
    print type(park_conf)
    for key, value in park_conf.items():
        # print "%s, %s"%(key, value) + str(type(value))
        print repr(key), repr(value)

    print "reids chset==========="
    park_name = park_conf['park_name']
    print park_name

    print "get device_conf id" + "="*20
    ret = get_reids_conf(redis.r, "device_conf", "id")
    ret_1 = get_reids_conf(redis.r, "device conf", "id")

    print "get reid by python ret" + "="*20
    print ret, ret_1
    '''


    q = RedisQueue("test")

    # while q.empty():
    q.pull("12345688")
    print q.get()

    time.sleep(15)
