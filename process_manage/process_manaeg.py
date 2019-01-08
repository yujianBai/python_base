#coding:utf-8

from subprocess import check_output
import datetime
import os

def get_pricess_pid(processname):
    return map(int, check_output(["pidof", processname]).split())

def get_kill_pid(pid_list):
    pid_list.sort(reverse=True)
    # print "pid_list get_kill_pid", pid_list
    return pid_list[:-1]

def kill_big_sampid(pid_list):
    print "pid_list: ", pid_list

    if len(pid_list) > 2:
        big_pid = get_kill_pid(pid_list)
        for kpid in big_pid:
            print "kill pid: ", kpid
            os.system("kill %d"%kpid)
    else:
        print "no pid should be killed"

if __name__ == "__main__":
    print "init pid manage start: ", datetime.datetime.now()
    kill_big_sampid(get_pricess_pid("vpr_server"))


