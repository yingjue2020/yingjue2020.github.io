Title: Frida : 在Android上简单使用
Date: 2020-03-29 20:22:06
Modified: 2020-03-29 20:22:06
Category: Reverse Engineering
Tags: Frida
Slug: frida-basic-usage-for-android

## 环境搭建
frida-server : 12.8.19

下载frida-server并解压
```bash
xz -d frida-server-12.8.19-android-arm64.xz
adb push frida-server-12.8.19-android-arm64 /data/local/tmp/frida-server-arm64
```

修改权限并启动frida-server
```bash
adb shell
cd /data/local/tmp
chown root:root frida-server-arm64
chmod a+x frida-server-arm64
./frida-server-arm64
```

## 遇到的问题

> Unable to preload: Unable to access process with pid 402 due to system restrictions; try `sudo sysctl kernel.yama.ptrace_scope=0`, or run Frida as root

解决方法：
```bash
magiskhide  disable
```

## 参考资料
- https://github.com/frida/frida/issues/824
