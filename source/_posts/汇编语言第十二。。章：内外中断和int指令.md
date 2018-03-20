---
title: 汇编语言第十二。。章：内外中断和int指令
date: 2018-01-05 00:33:03
tags:
	- 汇编语言
	- 笔记
categories: 汇编语言
---

# 汇编语言第十二。。章：内外中断和int指令
> 不再过多说中断是什么了，就是可以随时控制CPU停止当前的指令干其他的事的意思，下面内中断程序的步骤：  
> 1. 将程序写入0:200开始的空间内，同时把字符什么的也要定义进去。  
> 2. 设置中断向量表，前面是ip，后面是cs。注意高低位。  

## 单步中断的操作
1. 取得中断类型码
2. 标志寄存器入栈
3. 标志寄存器TF和IF置零，防止在中断程序中在中断。  
4. CS内容入栈
5. IP入栈
6. 根据中断类型码从中断向量表中设置中断程序的CS和IP。

## 中断处理程序的编写方法
1. 保存用到的寄存器
2. 处理中断
3. 恢复寄存器
4. iret

iret用来返回程序：操作为：  

	pop ip
	pop cs
	popf
目的是回到执行中断处理程序之前的执行点继续执行程序。

## 编写0号中断程序

	assume cs:code ss:satck ds:data
	code segment
	start:	mov ax,cs
				mov ds,ax
				mov si,offset do0	;ds:si指向do0中断程序部分
				mov ax,0
				mov es,ax
				mov di,200h
				mov cx offset do0end - do0
				cld
				rep movsb
				mov ax,0			;安装中断程序
				mov es,ax
				mov word ptr es:[0],200h
				mov word ptr es:[0+2],0
				
				mov ax,4c00h
				int 21h
				
	do0:		jmp short do0start
				db "overflow!"
				
	do0start:
				mov ax,cs
				mov ds,ax
				mov si,202h			;ds:si指向字符串
				mov ax,0b800h
				mov es,ax
				mov di,12*160+36*2	;es:di指向显存空间
				mov cx,9
			s:	mov al,[si]
				mov es:[di],al
				inc si
				add di,2
				loop s
				
				mov ax,4c00h
				int 21h


## 中断的特殊情况
设置栈的操作不会响应中断，因为中断会进行栈操作，需要设置正确的栈顶，所以设置sp的指令应当紧接着设置ss的指令

## int指令
格式：int n，n为中断类型码  
int指令的最终功能和call类似，都是调用一段程序。   
中断处理程序简称为中断例程  

## 编写供应用程序调用的中断例程
明天再写详细的

## BIOS和DOS多提供的中断例程的安装过程
1. CPU加电，初始化(CS) = 0FFFFH，(IP) = 0，从FFFF：0开始执行程序。此处有一条跳转指令，跳转后开始执行BIOS中的硬件系统检测和初始化程序  
2. 初始化程序建立BIOS所支持的中断向量表，只需登记中断向量表，中断程序在ROM中，一直在内存中存在  
3. 硬件检测和初始化完成之后，调用int 19h，进入操作系统引导程序。
4. DOS启动，将所提供的中断例程装入内存，并建立中断向量表。


## BIOS和DOS的中断例程的应用
就是应用了，比如BIOS中的彩色显示int 10h和DOS中的输出字符串int 21h。明天再写

## 汇编语言：完～