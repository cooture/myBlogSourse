---
title: '汇编第五章 [BX]和loop指令'
date: 2017-12-28 20:07:35
tags:
	- 汇编语言
	- 笔记
categories: 汇编语言
---

# 汇编第五章 [BX]和loop指令

**[bx]**表示偏移地址  
**ss:ip**   表示栈段  
**push ax**的具体流程  
		
	push ax:
	sp = sp - 2;
	(ss:sp) = ax;

**pop ax**的具体操作  

	pop ax:
	ax = (ss:sp);
	sp+=2;  
	
**inc ax**  ax的内容加1  

**mov ax,2000H**   其中ah = 20 al = 00  

	当
	BE   21000H
	00   21001H
	.
	.
	.
	
	mov ax,2100H;
	mox dx,ax;
	mov bx,0;
	mov ax,[bx]
	
	此时 ax = 00BE
！！意为先存低位，在存高位。  

## LOOP指令  
**LOOP执行顺序**

	LOOP执行顺序：
	1.CX--;
	2.CX==0?顺序执行:循环

**CX设置循环次数**
	
	  例如：
	  mov cx,11
	L:add ax,1
	  LOOP L

**将ffff传入ax中的时候要前面加零**

	mov ax,0ffffH
	mov dx,ax
	.
	.
	.
**汇编语言程序中，数据不能以字母开头**
## DEBUG和汇编编译器MASM对指令的不同处理

**DEBUG中：**  
*mov al,[0]* ;含义：(al) = ((dx)*16+0)  
**源程序中:**	 
*mov al,[0]* ;含义：(al) = 0  
>在源程序中，如果用指令访问一个内存单元，则在指令中必须用“[...]”来表示内存单元
>，如果在“[]”里直接用一个常量idata直接给出内存单元的偏移地址，就要在"[]"的前面
>显示的给出段地址所在的段寄存器。  

例如：
	
	mov ax,dx:[0]
## 段前缀
以上这样的表示方法dx叫做**段前缀**  
类似的比如  
	
	mov ax,ds:[0]
	mov ax,cx:[0]
	mov ax,ss:[0]
	mov ax,es:[0]

等等ds:、cx:、ss:、es:、都叫做段前缀  

## 一段安全的空间  
直接向内存中写入数据时，要用：  
**0:200 ～ 0:2ff**  

	 
	 
	 
	 
	 
	 
	 
	 
	 
	 