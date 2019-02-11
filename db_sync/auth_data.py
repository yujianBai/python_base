#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: auth_data.py
@time: 2018/11/20 10:06
"""
from log import log

def auth_share(db_data, db_obj_local, table_name):
    #简便处理，更新授权信息， 先清理

    sql = 'delete from %s'%table_name
    db_obj_local.execute(sql)
    for item in db_data:
        ins_data = dict(
          op_type = item['op_type'],
          op_time = str(item['op_time']),
          # save_time = str(item['save_time']),
          depot_id = item['depot_id'],
        )
        try:
            db_obj_local.insert(table_name, ins_data)
        except Exception as error:
            log.info('insert error:%s'%error)

def auth_group(db_data, db_obj_local, table_name):

    sql = 'delete from %s'%table_name
    db_obj_local.execute(sql)
    for item in db_data:
        ins_data = dict(
          save_time = str(item['save_time']),
          depot_id = item['depot_id'])
        try:
            db_obj_local.insert(table_name, ins_data)
        except Exception as error:
            log.info('insert error:%s'%error)
