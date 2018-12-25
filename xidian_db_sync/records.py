#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: db_sync.py
@time: 2018/11/20 10:01
"""


def sync_records_inout(db_data, db_obj_local, table_name):
    for item in db_data:
        ins_data = dict(
        trace_uk = item['trace_uk'],
        in_time = str(item['in_time']),
        in_vpr_card = item['in_vpr_card'],
        in_vpr_plate = item['in_vpr_plate'],
        in_vpr_plate_color = item['in_vpr_plate_color'],
        in_vpr_pic_full = item['in_vpr_pic_full'],
        in_vpr_pic_plate = item['in_vpr_plate_slave'],
        in_vpr_plate_slave = item['in_vpr_plate_slave'],
        in_vpr_pic_full_slave = item['in_vpr_pic_full_slave'],
        in_vpr_pic_plate_slave = item['in_vpr_pic_plate_slave'],
        in_vpr_plate_color_slave = item['in_vpr_plate_color_slave'],
        in_used_plate = item['in_used_plate'],
        in_used_plate_color = item['in_used_plate_color'],
        in_depot_id = item['in_depot_id'],
        in_site_name = item['in_site_name'],
        in_auth_type = item['in_auth_type'],
        in_state_details = item['in_state_details'],
        in_state = item['in_state'],
        in_operate_time = str(item['in_operate_time']),
        in_operator = item['in_operator'],
        # park_in_id = item['park_in_id'],
        # park_out_id = item['park_out_id'],
        out_vpr_plate = item['out_vpr_plate'],
        out_vpr_card = item['out_vpr_card'],
        out_time = str(item['out_time']),
        out_vpr_plate_color = item['out_vpr_plate_color'],
        out_vpr_pic_full = item['out_vpr_pic_full'],
        out_vpr_pic_plate = item['out_vpr_pic_plate'],
        out_vpr_plate_slave = item['out_vpr_plate_slave'],
        out_vpr_pic_full_slave = item['out_vpr_pic_full_slave'],
        out_vpr_pic_plate_slave = item['out_vpr_pic_plate_slave'],
        out_vpr_plate_color_slave = item['out_vpr_plate_color_slave'],
        out_used_plate = item['out_used_plate'],
        out_depot_id = item['out_depot_id'],
        out_site_name = item['out_site_name'],
        out_auth_type = item['out_auth_type'],
        out_state_details = item['out_auth_type'],
        out_state = item['out_state'],
        out_stopping_time = str(item['out_stopping_time']),
        out_should_pay = item['out_should_pay'],
        out_remarks = item['out_remarks'],
        out_operate_time = str(item['out_operate_time']),
        out_operator = item['out_operator'],
        out_open_time = str(item['out_open_time']),
        out_total_price = item['out_total_price'],
        self_depot_fee = item['self_depot_fee'],
        vehicle_type = item['vehicle_type'],
        power_type = item['power_type'],
        logo = item['logo'],
        vehicle_model = item['vehicle_model'],
        body_color = item['body_color'],
        in_taxprinted = item['in_taxprinted'],
        taxprinted = item['taxprinted'],
        now_time = str(item['now_time']),
        )
        try:
            db_obj_local.insert(table_name, ins_data)
        except Exception as error:
            log.info('insert records error:%s'%error)

