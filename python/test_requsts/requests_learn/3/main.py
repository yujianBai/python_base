# -*- coding: utf-8 -*-
# @Time    : 19-5-9 下午11:29
# @Author  : Baiyj

# @File    : main
import json

import requests

URL = "http://api.github.com"

def build_url(endpoint):
    return '/'.join([URL, endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def request_method():
    response = requests.get(build_url("users/imoocdemo"))
    print better_print(response.text)

if __name__ == "__main__":
    request_method()