#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: change_value.py.py
@time: 2019/4/13 14:55
"""

#get_para_from_stdin
import random

def change(pata_list):
    num = 0
    change_flag = False
    ins_id = 0
    for item in pata_list:
        print('-----------------get item is :%d'%item)
        if item != num:
            num = item
            change_flag = True
        else:
            continue
        if change_flag:
            if ins_id == 0 and num:
                ins_id = random.randint(0, 100)
                print ("insert:%d"%ins_id)
            elif num == 0 and ins_id:
                print ("update:%s"%ins_id)
                ins_id = 0
            elif num and ins_id:
                print ("update:%s"%ins_id)
                ins_id = 0
                ins_id = random.randint(0, 100)
                print ("insert:%d"%ins_id)
            change_flag = False

if __name__ == "__main__":
    # change([1, 1, 0])
    # change([1, 1, 2, 0])
    # change([1, 1, 1, 2, 0, 0, 0])
    # change([0, 0, 1 ,0 ,2, 0, 0, 3])
    change([0, 0, 1 ,0 ,2, 0, 0, 3, 0])


