---
title: hexo自动发布部署同步脚本
tags: []
categories:
  - hexo
originContent: ''
toc: true
date: 2019-04-20 02:21:01
---

# hexo自动发布脚本

> 自动编译上传GitHub服务器，同时让自己的服务其同步的python脚本

```python
import os
import threading

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
        print('运行成功')
        ssh.close()
        print('关闭连接')
    except Exception as error:
        print(error)


if __name__ == '__main__':
    ip = "ip" # TODO:
    name = "name" # TODO:
    pwd = "pwd" # TODO:
    cmd_local = "cd ~/Documents/blog;hexo g -d"
    cmd_host = ["cd /data/ranxuebin/;git pull;"]
    os.system(cmd_local)
    a = threading.Thread(target=execute_cmds, args=(ip, name, pwd, cmd_host))
    a.start()
```