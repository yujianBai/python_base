#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: db_sync.py
@time: 2018/11/20 10:01
"""


def sync_records_inout(db_data, db_obj_local, table_name):
    for item in db_data:
        ins_data = dict(
        body_color = item['body_color'],
        in_taxprinted = item['in_taxprinted'],
        now_time = str(item['now_time']),
        )
        try:
            db_obj_local.insert(table_name, ins_data)
        except Exception as error:
            log.info('insert records error:%s'%error)

