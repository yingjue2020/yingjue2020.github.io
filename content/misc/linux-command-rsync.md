Title: Linux常用命令工具使用笔记
Date: 2020-03-24 17:46:35
Modified: 2020-03-24 17:46:35
Category: Misc
Tags: Linux
Slug: linux-common-command
Figure: linux.png

**find**

在当前目录下查找某个文件：
```bash
find -name "lib*.a"
```

**rsync**

Linux 下合并两个目录，软连接也一起同步。
```bash
rsync -K -a 源目录  被覆盖目录
```

比如：
```bash
rsync -K -a dir1/ dir2/
```

统计文件个数
```bash
Linux: ls -1 data/devices|wc -l
Windows: dir /b /a-d xxx|find /v /c “”
```

lldb
```bash
dis --start-address 0x190885710 --count 10
dis -n "-[NSBundle bundleIdentifier]"
memory read 0x190885710 --format x --count 20 --size 1
```

Start Local HTTP Server
```bash
python3 -m http.server --directory ./
```

Wireshark
```bash
Install “Network Commands” from Cydia
tcpdump -i any -w /var/tmp/capture.pcap
tcpdump -i any -w /var/tmp/sample-20240717-1.pcap
scp -P 2222 root@127.0.0.1:/var/tmp/sample-20240717-1.pcap .
ip.addr[0]==67 || ip.addr[0]==cb || ip.addr[0]==77 || ip.addr[0]==65
```

**Configuration**

.bash_profile
```bash
#ADDED BY 010 EDITOR
export PATH="$PATH:/Applications/010 Editor.app/Contents/CmdLine"
. "$HOME/.cargo/env"
```

.zprofile
```bash
export PATH="$PATH:$HOME/flutter/bin"

export GEM_HOME=$HOME/.gem
export PATH=$GEM_HOME/ruby/2.6.0/bin:$PATH

export IDAUSR=$HOME/.idapro:$HOME/projects/learnida

export JAVA_HOME=`/usr/libexec/java_home -v 17`

alias java-17=”export JAVA_HOME=`/usr/libexec/java_home -v 17`”
alias java-11=”export JAVA_HOME=`/usr/libexec/java_home -v 11`”

export ANDROID_SDK=$HOME/Library/Android/sdk
export PATH=$ANDROID_SDK/platform-tools:$PATH

eval "$(/opt/homebrew/bin/brew shellenv)"
```

.zshrc
```bash
export PATH="/opt/homebrew/opt/openssl@1.1/bin:$PATH"
export THEOS=$HOME/theos

export MonkeyDevPath=/opt/MonkeyDev
export MonkeyDevDeviceIP=
export PATH=/opt/MonkeyDev/bin:$PATH
export PATH=$HOME/.docker/bin:$PATH
```

.zshenv
```bash
. "$HOME/.cargo/env"
export THEOS=~/theos
export THEOS=~/theos
```

zip format
```bash
1F 8B 08 00 72 B4 87 66  02 FF AB 56 4A 4A 4D 4C
2 bytes  GZIP标志字节：0x1f, 0x8b (\037 \213)  
1 byte   压缩方法： (0..7 reserved, 8 = deflate)
1 byte   标志位：
            bit 0 set: 文件可能是ASCII文本文件
            bit 1 set: 附加多个gzip文件部分
            bit 2 set: 存在有可选的附加 内容
            bit 3 set: 提供了原始的文件名称
            bit 4 set: 则提供有一个O－终结的文件内容
            bit 5 set: 文件被加密
            bit 6,7:   保留
4 bytes  文件更改时间(Unix时间)
1 byte   额外的标志，决定了压缩方法。 2:使用最大的压缩，最慢的算 4:采用最快的算法 02 vs 00
1 byte   这个标志指明了进行压缩时系统的类型。FF vs 13
                 0 - FAT filesystem (MS-DOS, OS/2, NT/Win32)
                 1 - Amiga
                 2 - VMS (or OpenVMS)
                 3 - Unix
                 4 - VM/CMS
                 5 - Atari TOS
                 6 - HPFS filesystem (OS/2, NT)
                 7 - Macintosh
                 8 - Z-System
                 9 - CP/M
                10 - TOPS-20
                11 - NTFS filesystem (NT)
                12 - QDOS
                13 - Acorn RISCOS
               255 - unknown
```

**参考链接**

- https://linux.die.net/man/1/rsync

