#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: sync_data.py
@time: 2018/11/20 14:11
"""
import datetime
import os

from records import sync_records_inout
from auth_data import auth_share, auth_group
from base_db import Mysql
from log import log

def get_auth_share_data(host, port=3306):
    handle = Mysql(host = host, user='root', passwd='passwd', port = port)
    sql = 'select * from new_auth_share;'
    data = handle.execute(sql)
    return data

def get_auth_group_data(host, port = 3306):
    handle = Mysql(host = host, user='root', passwd='passwd', port = port)
    sql = 'select * from new_auth_group;'
    data = handle.execute(sql)
    return data

def count_auth_share(host, port =3306, table = 'new_auth_share'):
    handle = Mysql(host = host, user='root', passwd='passwd', port = port)
    sql = 'select count(*) as cnt from %s;'%table
    data = handle.execute(sql)
    if data:
        return int(data[0]['cnt'])
    else:
        return 0

def get_yestorday(days =1):
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=days)
    return str(yesterday)[:10]

def get_records_data(host, port = 3306):
    handle = Mysql(host = host, user='root', passwd='passwd', port = port)
    yesterday = get_yestorday()
    sql = "select * from records_inout where out_time between '%s' and '%s'  and out_time != '0000-00-00 00:00:00' and in_time != '0000-00-00 00:00:00';"%(yesterday+ ' 00:00:00', yesterday + ' 23:59:59')
    data = handle.execute(sql)
    return data


def sync_data():
    tablenames = [('sourth', ip1),
                  ('north', ip2),
                  ('employees', ip3]
    localhost = localhost
    localport = 13306
    db_handle = Mysql(host = localhost, port = localport, user='xidian', passwd='passwd')

    for tablename, remotehost in tablenames:
        localtable = 'new_auth_share_'+tablename
        local_share_count = count_auth_share(host = localhost, port=localport,  table = localtable)
        remote_share_count = count_auth_share(remotehost)
        log.info('remote_share_count:{}, local_share_count:{}'.format(remote_share_count, local_share_count))
        if  remote_share_count != local_share_count or local_share_count == 0:
            group_data = get_auth_group_data(remotehost)
            auth_group(group_data, db_handle, 'new_auth_group_'+tablename)

            share_data = get_auth_share_data(remotehost)
            auth_share(share_data, db_handle, 'new_auth_share_'+tablename)

        record_data = get_records_data(remotehost)
        sync_records_inout(record_data, db_handle, 'records_inout_'+tablename)

def clear_log():
    last_day = get_yestorday(days=7)
    last_log =  './sync_data_%s.log'%last_day

    log.info('last_day:{}, last_log:{}'.format(last_day, last_log))
    if os.path.exists(last_log):
        log.info('clear log file:{}'.last_lot)
        os.remove(last_log)

if __name__ == '__main__':
    clear_log()
    sync_data()
