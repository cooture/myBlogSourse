---
title: Mac OS下SD卡烧录镜像
date: 2018-06-05 11:21:57
tags: [烧录,SD卡,Mac]
categories: 烧录
---
# Mac OS下SD卡烧录镜像

> 经常换镜像，做个笔记。

## 格式化
打开磁盘管理，选择SD卡，全部抹除，格式为FAT，不在多说。

## 卸载分区
* 打开命令行
`diskutil list` 查看设备列表

```shell
Rankin-Mac:~ Rankin$ diskutil list
/dev/disk0 (internal):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                         500.3 GB   disk0
   1:                        EFI EFI                     314.6 MB   disk0s1
   2:                 Apple_APFS Container disk1         500.0 GB   disk0s2

/dev/disk1 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +500.0 GB   disk1
                                 Physical Store disk0s2
   1:                APFS Volume Macintosh HD            215.0 GB   disk1s1
   2:                APFS Volume Preboot                 24.2 MB    disk1s2
   3:                APFS Volume Recovery                517.8 MB   disk1s3
   4:                APFS Volume VM                      3.2 GB     disk1s4

/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *7.9 GB     disk2
   1:                 DOS_FAT_32 UNTITLED                7.9 GB     disk2s1

/dev/disk3 (disk image):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        +314.8 GB   disk3
   1:                        EFI EFI                     209.7 MB   disk3s1
   2:                  Apple_HFS 时间机器备份            314.5 GB   disk3s2

```
这样的就卸载disk2的所有分区，例如disk2s1，有多的都要卸载。

* 命令：`diskutil unmount /dev/disk2s1`

## 烧录
前提是准备好你的镜像iso文件。

* 命令：`sudo dd bs=4m if=ubuntu-16.04.4-lxqt-aarch64-raspberrypi3b-raspberrypi3b-plus-20180428-chainsx.img of=/dev/rdisk2`
* 注意，目标磁盘为原始磁盘rdisk*，绝对不要把数字写错。

完成后会提示

```
750+0 records in  
750+0 records out
3145728000 bytes transferred in 279.701624 secs (11246728 bytes/sec)
```

## 卸载磁盘
* 命令：`diskutil unmountDisk /dev/disk2`
* 完成