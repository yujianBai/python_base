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
          auth_no = item['auth_no'],
          vpr_plate = item['vpr_plate'],
          vpr_plate_noword = item['vpr_plate_noword'],
          vpr_card = item['vpr_card'],
          remark = item['remark'],
          is_occupied = item['is_occupied'],
          is_in = item['is_in'],
          # in_time = str(item['in_time']),
          # auth_takeeffect_time = str(item['auth_takeeffect_time']),
          serial_no = item['serial_no'],
          register = item['register'],
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
          auth_no = item['auth_no'],
          auth_type = item['auth_type'],
          sday = str(item['sday']),
          eday = str(item['eday']),
          time_range = str(item['time_range']),
          week = item['week'],
          is_share = item['is_share'],
          share_tol = item['share_tol'],
          holder_name = item['share_tol'],
          phone = item['share_tol'],
          address = item['address'],
          email = item['email'],
          remarks = item['remarks'],
          valid_flag = item['valid_flag'],
          nested = item['nested'],
          msg_json = item['msg_json'],
          serial_no = item['serial_no'],
          register = item['register'],
          op_type = item['op_type'],
          op_time = str(item['op_time']),
          save_time = str(item['save_time']),
          depot_id = item['depot_id'])
        try:
            db_obj_local.insert(table_name, ins_data)
        except Exception as error:
            log.info('insert error:%s'%error)
