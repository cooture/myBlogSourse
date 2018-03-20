---
title: 无显示器条件下查询树莓派IP的方法
date: 2018-02-14 12:18:09
tags: [树莓派,Unix]
categories: 树莓派
---

# 无显示器条件下查询树莓派IP的方法
> 方法都根据树莓派的网卡物理地址为`b8:27:eb:`开头	。因此有以下自动化方法

## Mac下打开网络实用工具

直接查询Netstat下的路由表找到树莓派的物理地址对应的就是树莓派的IP地址。

## Shell脚本
> 整个代码逻辑为依次pingIP地址，之后通过arp映射找到对应的物理地址，取到对应的IP。

代码如下

	clear
	
	
	echo "程序运行中..."
	ipLine="`ifconfig | grep "inet 192.168" `"
	preIp=${ipLine:5:11}
	echo "程序默认将在$preIp 2 - $preIp 255范围内进行扫描"
	echo "但这将花费较多时间，请问是否进行手动设置？（y/n)"
	read choice
	if test $choice = "y"
		then
			echo -n "请输入起始位置(2-255):"
			read i
			echo -n "请输入结束位置($i-255):"
			read j
			echo "下面将对 $i 到 $j 范围进行扫描"
		else
			i=2
			j=255
			echo "下面将直接对2-255整个范围进行扫描"
	fi
	while test $i -ne $j
	do
		echo "正在检测ip的连接情况，请耐心等待"
		ip=$preIp$i
		echo "正在ping端口$ip ..."
		"`ping -t 1 -q $ip `"
		let i=i+1
		clear
	done
	clear
	echo "所有ip检测完毕，正在计算结果..."
	result="`arp -a | grep "b8:27:eb:" ` "
	resultIp=${result:3:14}
	resultMac=${result:19:17}
	clear
	echo "已经得到结果："
	echo "您的树莓派Mac地址为:$resultMac"
	echo "    当前连接的IP为:$resultIp"
	echo
	echo "程序结束"