"""
__author__ = 'Rankin'
__mtime__ = '2019-04-19'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import os
import threading
import sys
import paramiko


def execute_cmds(ip, name, pwd, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, name, pwd, timeout=5)
        print('连接成功')

        for m in cmd:
            print(m)
            stdin, stdout, stderr = ssh.exec_command(m)
            out = stdout.readlines()
            for o in out:
                print(o)
        ssh.close()
        print('关闭连接')
    except Exception as error:
        print("something error!")
        print(error)


if __name__ == '__main__':
    arg = sys.argv
    if len(arg)-1:
        arg = arg[1]
    ip = "ranxb.com"
    name = "root"
    pwd = "wsr@n1234"
    cmd_local = "cd /Users/mac/Documents/blog ; hexo g -d"
    cmd_host = ["cd /home/rankin/www/ranxuebin ; git pull;"]
    if arg != 'd' and arg != 'r':
        print("starting push ranxb.cn")
        os.system(cmd_local)
    print("strating push ranxb.com")
    a = threading.Thread(target=execute_cmds, args=(ip, name, pwd, cmd_host))
    a.start()

