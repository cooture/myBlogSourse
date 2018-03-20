---
title: Ubuntu上启动ftp服务
date: 2018-02-07 21:13:49
tags: [Linux,FTP]
categories: Linux
---
# Ubuntu上启动ftp服务

## 安装并启动VSFTPD
* 安装VSFTPD
`sudo apt-get install vsftpd -y`
* 启动VSFTPD(会自动启动若未启动)
`sudo systemctl start vsftpd.service`
* 检测端口，判断是否启动。
`sudo netstat -nltp | grep` 

## 配置用户访问目录
* 新建主目录
* 新建用户并设置密码
`sudo useradd -d /home/uftp -s /bin/bash uftp`
`sudo passwd uftp`
`sudo rm /etc/pam.d/vsftpd`(这里删除该配置文件，因为会导致使用用户名登录FTP失败)
* 限制用户只能通过FTP访问
`sudo usermod -s /sbin/nologin uftp`
* 修改VSFTPD配置
`sudo chmod a+w /etc/vsftpd.conf`
下面修改`/etc/vsftpd.conf `文件中的配置（添加到最下面）

		# 限制用户对主目录以外目录访问
		chroot_local_user=YES
		
		# 指定一个 userlist 存放允许访问 ftp 的用户列表
		userlist_deny=NO
		userlist_enable=YES
		
		# 记录允许访问 ftp 用户列表
		userlist_file=/etc/vsftpd.user_list
		
		# 不配置可能导致莫名的530问题
		seccomp_sandbox=NO
		
		# 允许文件上传
		write_enable=YES
		
		# 使用utf8编码
		utf8_filesystem=YES
新建文件`/etc/vsftpd.user_list`用于存放允许访问FTP的用户
`sudo touch /etc/vsftpd.user_list`
`sudo chmod a+w /etc/vsftpd.user_list`
并修改，加入刚刚创建的用户

* 设置访问限权  
设置主目录访问权限（只读）：`sudo chmod a-w /home/uftp`
设置公共目录，设置可读写：`sudo mkdir /home/uftp/public && sudo chmod 777 -R /home/uftp/public`
重启VSFTPD服务：`sudo systemctl restart vsftpd.service`

## 完
