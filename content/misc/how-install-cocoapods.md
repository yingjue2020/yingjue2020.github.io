Title: 如何安装cocoapods
Date: 2024-11-29 17:34:15
Modified: 2024-11-29 17:34:15
Category: iOS
Tags: cocoapods
Slug: how-install-cocoapods
Figure: xcode.png

Cocoapods 是iOS开发的包管理工具。在Mac 14.6.1 上的安装过程如下：

- 安装brew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- 安装ruby
```bash
brew install ruby
```

一定要用brew安装ruby，系统自带的ruby安装不会成功，会产生很多错误，比如版本不匹配：

> The last version of drb (>= 0) to support your Ruby & RubyGems was 2.0.6. Try installing it with `gem install drb -v 2.0.6` and then running the current command again
> drb requires Ruby version >= 2.7.0. The current ruby version is 2.6.10.210.

- 修改.zprofile

在~/.zprofile文件末尾增加如下内容：
```bash
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
export GEM_HOME=$HOME/.gem
export PATH=$GEM_HOME/ruby/3.3.0/bin:$PATH
```

- 安装cocoapods

```bash
gem install cocoapods --user-install
```

- 测试是否安装成功

```bash
pod --version

# Output
1.16.2
```