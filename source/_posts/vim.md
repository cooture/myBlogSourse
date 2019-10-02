---
title: vim笔记
tags: [vim, linux]
date: 2019-09-30 19:00:51
categories: [vim]
---

# Vim 笔记

## 编辑

* i——insert（字母前）
* a——append（字母后）
* o——below（下一行）
* A——append after line（行后）
* I——insert before line（行前）
* O——above line（上一行）



- ctrl+u——删除行
- ctrl+w——删除字
- ctrl+a——移动到最前
- ctrl+e——移动到最后
- gi——移动到上一次编辑的地方 



* dw——删除一个字符
* dd——删除一行
* dt{char}——删除到某个字符
* d0/$——删除到行首行尾
* x——删除字符



快速修改

* r（replace）——替换
* c（change）——ct“——删除到”之前的内容并进入编辑模式
* s（substitute）——删除并进入编辑模式



替换

* `:% s/self/this/g`——%全部，s替换，self替换为this，g全局
* `:1,6 s/self/this/c`——1，6行，s替换，sels替换为this，c需要确认



查询

* /？——前向或反向
* nN——下一个或者上一个



## 视图

- `:vs`——左右分屏
- `:sp`——上下分屏
- `:q`——退出屏幕



- v——选中模式
- V——行选中
- ctrl+v——块选中
- y——复制
- p——粘贴
- u——撤销
- d——删除



## 移动

- hjkl——上下左右
- w/W 移到下一个单词开头，大写以空格为分割
- e/E移到下一个单词的结尾
- b/B上一个开头

行间移动

- f{char}——行内搜索并跳转到下一个字母上，F表示向前搜索



* 行首行尾——0，$



* gg/G——文件开头/结尾
* H/M/L——屏幕开头/中间/结尾
* ctrl+u/f——向上/下翻页
* z z——放在中间



## 配置



