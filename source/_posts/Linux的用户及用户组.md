---
title: Linux的用户及用户组
date: 2018-02-07 21:12:41
tags: [Linux,用户]
categories: Linux
---

# Linux的用户及用户组
## 配置文件

* `/etc/group`  组信息配置文件
* 	`/etc/passwd` 用户信息配置文件
* `/etc/shadow` 用户密码配置文件
* `/etc/gshadow` 组密码配置文件

![](a.jpg)   
![](b.jpg)

## 基本操作
### 组操作
`groupadd NEWGROUP`添加一个组  
`groupadd -g 888 NEWGROUP`添加一个组并指定UID   
`grouddel NEWGROUP`删除一个组。
`groupmod -n NEWGROUP OLDGROUP`更改组名
`groupmod -g 888 NEWGROUP`更改组UID
### 用户操作
`useradd -g GROUP USER`添加一个指定用户组的用户
`useradd -d /home/xxx USER`添加一个指定目录的的用户
`userdel USER`删除一个用户
`userdel -r USER`同时删除用户主目录
`usermod -l NEWNAME USER`更改用户名
`usermod -c BEIZHU USER`加备注
`usermod -d /home/yyy UESR`改用户主目录
`usermod -g GROUP USER`改组


> 在`/etc/`下创建`nologin`文件其他用户均不能登录

## 进阶操作
### 组
> 主要组和附属组

`gpasswd -a USER GROUP,GROUP2`添加附属组
`newgrp GROUP`切换用户组,此时可能需要组密码
`gpasswd -d USER GROUP`删除附属组
`useradd -g 主要组 -G 附属组，附属组 USER`新建时指定用户组
`gpasswd GROUP`修改组密码


### 用户
`passwd -l USER`锁定账户
`passwd -u USER`解锁账户
`passwd -d USER`清除密码

## 其他命令
`su USER` 切换账户


