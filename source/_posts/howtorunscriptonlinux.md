---
title: linux后台运行脚本的指令
tags: []
categories:
  - 脚本
toc: true
date: 2019-07-19 21:27:14
---

> 写给RoseauHan的

## How
举个栗子

`sudo nohup python3 -u AppleDeliverMail.py > log & echo $! > pid`

## Why
nohup一般是需要挂后台长时间执行的脚本用的。
bg和fg指令只用于切换终端的前后台进程，如果终端断开连接，脚本也会被退出，所以长时间的脚本一般情况用nohup指令

## Stop
命令后面会保存pid到文件中，所以不用担心pid找不到（找不到就ps呗，但是我还是喜欢记下来），终止的时候kill掉就好了