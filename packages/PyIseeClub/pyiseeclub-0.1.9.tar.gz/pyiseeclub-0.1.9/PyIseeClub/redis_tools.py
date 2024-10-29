# -*- coding: utf-8 -*-

import redis


def redis_conn(host='localhost', db=0):
    pool = redis.ConnectionPool(host=host, port=6379, db=db, decode_responses=True)
    rd = redis.Redis(connection_pool=pool)
    return rd


def set_value(db, key, value):
    rd = redis_conn(db=db)
    rd.set(key, value)
    rd.close()


def get_value(db, key):
    rd = redis_conn(db)
    result = rd.get(key)
    rd.close()
    return result


def delete_value(db, key):
    rd = redis_conn(db)
    rd.delete(key)
    rd.close()
