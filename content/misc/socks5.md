Title: SOCKS5
Date: 2024-09-25 10:33:00
Modified: 2024-09-25 10:33:00
Category: Misc
Tags: socks5, shadowsock
Slug: socks5
Figure: socks5.png

socks是一种互联网协议，它通过一个代理服务器在客户端和服务端之间交换网络数据。

简单来说，它就是一种代理协议，扮演一个中间人的角色，在客户端和目标主机之间转发数据。

socks协议位于OSI模型中的第五层，即会话层(Session Layer)。

对于广大的中国网友来说，一提到代理，肯定会想到翻墙，而socks5作为一种代理协议，肯定也能用来翻墙嘛。不过遗憾的是，虽然它是代理协议，然而并不能用于翻墙。因为它的数据都是明文传输，会被墙轻易阻断。

socks协议历史悠久，它面世时中国的互联网尚未成型，更别说墙，因此它并不是为翻墙而设计的协议。互联网早期，企业内部网络为了保证安全性，都是置于防火墙之后，这样带来的副作用就是访问内部资源会变得很麻烦，socks协议就是为了解决这个问题而诞生的。

socks相当于在防火墙撕了一道口子，让合法的用户可以通过这个口子连接到内部，从而访问内部的一些资源和进行管理。


## References
- [SOCKS5 协议原理详解与应用场景分析](https://www.cnblogs.com/chr1ce/articles/16246884.html)
- [Shadowrocket iOS IPA](https://github.com/JiangRongZhi/Shadowrocket-IOS)
- [Shadowrocket iOS sourcecode](https://github.com/XWJACK/Shadowrocket.git)
- [Tutorial for ShadowRocket app](https://hiddify.com/manager/client-software-on-ios/Tutorial-for-ShadowRocket-app/)
- [Shadowrocket Android APK](https://github.com/Pawdroid/shadowrocket_for_android)
- [Shadowrocket Android APK](https://github.com/shadowsocks/shadowsocks-android/releases)
- [理解socks5协议的工作过程和协议细节](https://wiyi.org/socks5-protocol-in-deep.html)
- https://github.com/shadowsocks
- https://github.com/shadowsocksrr
- [Understanding Shadowsocks](https://oliver-hu.medium.com/understand-shadowsocks-106105068778)