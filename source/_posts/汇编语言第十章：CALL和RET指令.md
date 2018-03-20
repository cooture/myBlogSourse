---
title: 汇编语言第十章：CALL和RET指令
date: 2018-01-04 23:33:06
tags:
	- 汇编语言
	- 笔记
categories: 汇编语言
---

# 汇编语言第十章：CALL和RET指令
> 都是修改ip的，重点不多，会用就行，随便写写。

## ret和retf
**ret进行近转移，只修改IP**  
**retf进行远转移，修改IP和CS**  
### ret指令的操作
**出栈操作**  
1. (IP) = ((ss)*16+sp)  
2. (sp) = (sp)+2  
相当于pop IP

### retf指令的操作
**先出ip，再出cs**  
1. (IP) = ((ss)\*16+sp)  
2. (sp) = (sp)+2  
3. (CS) = ((ss)*16+sp)  
4. (sp) = (sp)+2  
相当于pop ip；pop cs

## CALL指令
> 两步操作  
> 1. IP或CS和IP压入栈  
> 2. 转移

(CALL的转移位移是16位的，也就是短转移，不支持近转移)
### 根据位移进行转移的CALL指令
**先压栈，在转移**  
1. (sp) = (sp)-2  
2. ((ss)*16+sp) = ip  
3. ip转移  

格式：CALL 标号  

### 根据目的地址转移的CALL指令
格式： 
 
	call far prt 标号
实现的是段间转移  
执行此命令时进行如下操作：  
1. push CS
2. push IP
3. CS：IP转移

### 地址在寄存器中的CALL指令
格式： call 16位的reg  
例如： call ax  
相当于：  
push ip
jmp ax

### 转移地址在内存中的CALL指令
#### CALL WORD PRT 地址
两个字节16位，只转移IP
#### CALL DWOERD PRT 地址
四个字节32位，转移CS和IP

## RET和CALL的配合使用
当正常函数用，没什么区别  
要先push 前面用到的寄存器的值  
前面CALL，后面RET

## MUL指令
乘法指令，和除法指令类似，只是要不都是8位的，要不都是16位的。  
### 8位的
AL放一个，然后MUL一个8位的内存单元，结果放在AX里面  
如100*10:  
	
	mov al,100
	mov bl,10
	mul bl
最后结果在AX里  
或者mul一个内存单元，还是例如：

	mov al,100
	mov ds:[0],10
	mul byte ptr ds:[0]
### 16位的
AX放一个，然后MUL一个16位寄存器或者内存单元，结果高位在DX里，低位在AX里。  
例如1000*10：

	mov ax,1000
	mov bx,10
	mul bx
结果换成16进制，高位在DX里，低位在AX里。

**除法在第八章**







