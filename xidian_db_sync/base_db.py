#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: base_sb.py
@time: 2018/11/20 9:57
"""

#!/usr/bin/python
# -*- encoding: utf-8 -*-
import MySQLdb
import traceback
from log import log

class Mysql:
    def __init__(self,
                 host='192.168.55.100',
                 port=3306,
                 user='root',
                 passwd='root'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.charset = 'utf8'
        self.cursor = None
        self.conn = None
        self.connect()

    def connect(self, auto_commit=True):
        log.info(" mysql connect start")
        self.conn = MySQLdb.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            db = 'irain_park',
            port = self.port,
            charset = self.charset
        )
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        if auto_commit:
            self.conn.autocommit(True)
        log.info(" connect end I'm here")

    def escape(self, value):
        if type(value) == str:
            value = self.conn.escape_string(value)
            value = '"%s"' % value
        elif type(value) == unicode:
            value = value.encode(self.charset)
            value = self.conn.escape_string(value)
            value = '"%s"' % value
        else:
            value = str(value)
            value = self.conn.escape_string(value)
        return value

    def check_connect(self):
        try:
            self.conn.ping()
            return True
        except:
            log.warning("failed![sql:][%s]" % (traceback.format_exc()))
            log.info("check_connect failure,I'm here")
            return False

    def insert(self, table_name, data_dict):
        if not self.check_connect():
            self.connect()
        if data_dict is None or len(data_dict) == 0: return False
        keys = data_dict.keys()
        values = data_dict.values()
        for i in range(len(keys)):
            values[i] = self.escape(values[i])
        sql = 'INSERT INTO %s (%s) VALUES (%s)' % (table_name, ','.join(keys), ','.join(values))

        # log.info(str(sql.encode()))
        self.execute(sql)
        id = self.cursor.lastrowid
        return id

    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            # log.info('execute sql: {}, result: {}'.format(sql, res))
            return res
        except Exception as error:
            log.error('execute sql failed: {}, stack: {}'.format(error, traceback.format_exc()))
            return ()

    def __del__(self):
        if self.conn:
            self.conn.close()
