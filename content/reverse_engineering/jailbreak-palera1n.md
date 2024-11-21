Title: How to jailbreak iOS 16 using palera1n
Date: 2024-09-25 10:56:00
Modified: 2024-11-21 10:56:00
Category: Reverse Engineering
Tags: jailbreak, palera1n
Slug: jailbreak-palera1n
Summary: Building iOS environment for reverse engineering. How to jailbreak iOS 15~18 using palera1n. Install Sileo and frida .
Figure: palera1n.png

Q: **Build may be slow as Theos isn’t using all available CPU cores on this computer.**

参考链接：[Parallel Building](https://theos.dev/docs/parallel-building)

步骤：

```bash
brew install make
echo PATH=\"$(brew --prefix make)/libexec/gnubin:\$PATH\" >> ~/.zprofile
```

## Download palera1n

Download [palera1n](https://palera.in/download/?tab=macos) on Mac:
```bash
sudo /bin/sh -c "$(curl -fsSL https://static.palera.in/scripts/install.sh)"
```

## Rootless jailbreak
```bash
palera1n -l
```

If palera1n is not installed, please run command:
```bash
palera1n -f
```

## Install Sileo
Open palera1n app and then install Sileo .

- install ssh: Open Sileo app and search ssh,install ssh-server and ssh-client .
- install frida: https://build.frida.re

## Enable ssh root

Install iproxy: brew install libusbmuxd

On mac run command:
```bash
iproxy 2221 22
```

Connect to iPhone using ssh
```bash
ssh mobile@127.0.0.1 -p 2221
```

Enbale root user:
```bash
sudo passwd root
```

![palera1n enable ssh root]({static}/images/palera1n_enable_ssh_root.png)
