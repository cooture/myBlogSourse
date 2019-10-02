---
title: MySQL中文的坑
tags: []
categories: []
originContent: ''
toc: true
date: 2019-06-04 15:28:46
---

> 小程序准备上线了，为了保证稳定性和数据库的安全准备从sqlite迁移到mysql，结果我就日了狗了。。。。。

现象：mysql中文字段报错：比如：`Incorrect string value: ‘\xF0\x9F\x98\x83 <…’ for column ‘summary’ at row 1`    
问题：明显是编码错误，环境是Macos+python3+Django。和明显不是我的编码问题。于是直接进行数据库操作` insert into app_lzuuserinfo (anameu) values ("冉");`还是报错，说明是数据库的编码问题  
解决：

这tm我就要好好说道说道了。第一步百度，答案清一色的是该数据库编码格式为utf8，但是我的数据库就是utf8的。无语，陷入死胡同，于是总觉得是没有生效的问题反复使用和修改`set character_set_character=utf8;`
和mysqld.cnf。最后毫无用处。

第二步，roseahan去Google了一下。。。。于是看到了这篇文章：
> https://medium.com/@adamhooper/in-mysql-never-use-utf8-use-utf8mb4-11761243e434

mdzz....  
大概意思如下：mysql的utf8不是我们的UTF-8，他的utf8是3个byte的编码格式，我们的UTF-8是四个字节的编码格式，所以改了utf8也不可能生效，所以我不知道为什么大家清一色的去改utf8...而且文章提出是mysql一直以来的bug没有解决，官方给出的解决方案是使用`utf8mb4`编码，这里的才是我们使用的UTF-8编码格式，同时emoji也是使用的这种格式。同时这个bug解决不了，官方也一直没有“声张”，所以。。。。。nb。下面给出解决方案，可以的话还是去我刚才的网站看吧。

method：  
> https://mathiasbynens.be/notes/mysql-utf8mb4#utf8-to-utf8mb4
require：mysql > 5.5.3
1. 对于已存在的表：  
```
# For each database:
ALTER DATABASE database_name CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
# For each table:
ALTER TABLE table_name CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
# For each column:
ALTER TABLE table_name CHANGE column_name column_name VARCHAR(191) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
# (Don’t blindly copy-paste this! The exact statement depends on the column type, maximum length, and other properties. The above line is just an example for a `VARCHAR` column.)
```

2. Check the maximum length of columns and index keys自行检查最大长度
3. Modify connection, client, and server character sets
老规矩修改cnf
```
[client]
default-character-set = utf8mb4

[mysql]
default-character-set = utf8mb4

[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
```
都是utf8mb4，
4. 重启。
5. 再去检查一下数据库的编码，就没问题了。

> 吐槽：baidu is a shit！the same as 闭眼睛转发的人




