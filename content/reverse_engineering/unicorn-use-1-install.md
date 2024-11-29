Title: Unicorn使用笔记（一）：安装
Date: 2024-11-29 20:22:06
Modified: 2024-11-29 20:22:06
Category: Reverse Engineering
Tags: IDA Pro, Unicorn
Slug: unicorn-use-1-install
Figure: idapro.png

Unicorn 是一个模拟执行库，支持多个平台，在逆向工程中动态分析指令流程非常有用。

笔者某些IDA脚本需要依赖unicorn，今天在安装后，发现不能使用。2.1.0和2.1.1在使用mem_map直接导致IDA崩溃。

可能与Mac Pro的Apple silicon有关，回头查了以前使用的版本是 2.0.1.post1 。

2.0.1.post1的pip包会触发本地编译，需要做一些准备工作：

- 安装Xcode

在AppStore里直接安装Xcode即可。

- 安装cmake和pkg-conf

```bash
brew install cmake
brew install pkg-config
```

- 安装unicorn
```bash
mkdir learnida && cd learnida
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install unicorn==2.0.1.post1
```