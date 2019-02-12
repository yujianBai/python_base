#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: json_test.py
@time: 2019/2/12 17:36
"""

import json

config = dict(
    ip = "192.168.55.1",
    port = "88",
    active = "False",
)

config_json = json.dumps(config)
print config_json, type(config_json)


config_dict = json.loads(config_json)
print config_dict, type(config_dict)
