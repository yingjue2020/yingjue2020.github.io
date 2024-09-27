Title: 7z 解压文件名乱码
Date: 2019-05-11 23:12:27
Modified: 2019-05-11 23:12:27
Category: Misc
Tags: 7z, code, page
Slug: 7z-error-codes
Figure: windows.jpeg

## 问题描述
在Windows 7中文版系统上使用7z压缩一些文件后，然后在Windows 10 Pro英文版系统上解压，发现凡是文件名中包含中文，最后都是乱码。

## 原因
使用7z压缩文件时，对文件名的编码是采用Windows 系统默认字符集，而不是unicode编码。

## 解决方法

- 使用python重命名
先解压，然后使用如下代码重命名
```python
# -*- encoding:utf-8 -*-
import zipfile
if __name__ == "__main__":
    names = os.listdir(".")
    for name in names:
        new_name = name.encode("cp437").decode("gbk")
        os.rename(name,new_name)
```
在Windows下python对文件名编码使用cp437或者utf8，name 这个字符串是经过cp437解码得到的unicode。
unicode 转为 bytes 采用encode
bytes 转为 unicode 采用decode

- 在7z压缩时使用utf8编码文件名
```shell
7z a -tzip -mcu examples.zip examples/
```

## 代码页
在Windows 10 Pro 上默认的代码页是cp437 这个代码页不能表示中文字符
```python
# 标准输出的编码
sys.stdout.encoding
# 系统本地化设置的编码
locale.getpreferredencoding()
```

代码页这个东西太神奇了，还是采用mac或者linux吧。


