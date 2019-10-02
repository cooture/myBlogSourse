---
title: swfit_Simple_Guide
tags: [swift, Guide]
date: 2019-10-02 15:53:51
categories:
---

> 新建一个PlayGround，直接看实例代码

```swift
import AppKit//暂时没啥用的东西
var strTest = "Hello, playground"
var maybeNilTest:Int? = nil
var intTest:Int = 10
var setTypeTest:(Int?, String) = (1,"hahaa")
var setValue = (1,3)
var deepCopySetTest = setValue

//??表达式判断可为nil的值
print(maybeNilTest ?? 10)
print(strTest)
//字符串拼接
print("intTest： \(intTest)")
//元组索引
print(setTypeTest.0!)
//type函数
print(type(of: setTypeTest))

//元组赋值，非引用，deepCopy
deepCopySetTest.0 = 10
print(setValue)
print(deepCopySetTest)

//元组key
var setc:(name1:Int, name2:String) = (1,"haha")
// terminator 参数separator 参数
print(setc, setc.name1, separator:"  separator  ", terminator:"  terminator  \n")
//三元运算符
var d = (maybeNilTest == nil) ? 1 :maybeNilTest!
print(d)

//if sentence
var ifTestValue = 10
if ifTestValue > 10{
    print("ifTestValue is bigger than 10")
}else if ifTestValue == 10 {
    print("this is else if branch")
}else {
    print("this is else branch")
}

//可选项绑定
//maybeNilTest = 1
if let optionBindTest = maybeNilTest{
    print("optionBindTest value is :",optionBindTest)
}else{
    print("maybeNilTest is nil")
}

//隐式展开
//允许让变量在某些情况下可以赋值为空，但是保证输入输出和调用时w有值
var yinshizhankai:Int! = 10
var yinshizhankaiB : Int = yinshizhankai
print("yinshizhankai is 10: ", yinshizhankai!)
yinshizhankai = nil
print("yinshizhankai is nil: ", yinshizhankai ?? 1)
print("yinshizhankaiB: ", yinshizhankaiB)

//swich
var swichTest = 10
switch swichTest {
case 1...10://区间，后面继续h说，这个是闭区间，开区间可以是..<
    print("swichTest == 10")
    fallthrough
case 20:
    print("switchTest == 20 with fallthrough")
default:
    print("default")
}

//switch 元组匹配
var switchTestB = (1, 2)
switch switchTestB {
case var(1, num) where num > 1:
    print("this is (1, 2) num is \(num) and num > 1")
    num = 3
default:
    print("this is default")
}
print("this is (1, 2) num is \(switchTestB)")


// 区间
var rangeA = 1.5...5
var rangeB = 1..<5

//for
for item in rangeA{
    if item == 2{continue} // break一样
    print(item, terminator:"  ")
}
print()
for item in stride(from: 1, to: 6, by: 2).reversed(){
    print(item, terminator:"  ")
}

```

