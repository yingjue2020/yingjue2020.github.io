Title: Debug Android Framework with Android Studio
Date: 2019-06-05 09:53:06
Modified: 2019-06-05 09:53:06
Category: Android
Tags: Android
Slug: debug-android-framework-with-android-studio

# 背景
在阅读Android Framework代码时，有时需要动态调试加深理解，或者想调试某个API的实现原理（如startActivity）时，希望可以使用Android Studio调试，且可以对应到源码的每一行，故需要搭建一个调试环境。

# 可选方案

## 模拟器
下载并编译某个版本的源码，得到相应的image，加载进模拟器，然后将对应的源码导入到Android Studio。Android源码本身提供了一个工具，可以生成一个Android Studio工程。

## Google 真机
需要有一台Google系手机，查看该手机的版本去下载对应的源码，利用Android源码里的工具生成Android Studio工程文件，导入到Android Studio。

## 缺点
上面两个方法网上有一些教程，本人没有试过，不知道是否真的可行。由于这两个方案有几个缺点，故而未使用。
- 本人不喜欢使用模拟器作为开发和调试环境。
- 下载一份Android源码时间太久，至少需要100G的硬盘空间。
- 不能在Windows系统调试。

# 方法
本节描述笔者使用的方法，该方法占用空间小、搭建时间短，可以在Windows系统上使用。本方法要求具备一台Google系手机，当然其他手机也可以，前提是该手机的框架层代码未被手机厂商修改过。

在Android Studio里如果想查看某个函数（如startActivity）的实现，可以右键跳转到源文件，前提是你下载了对应版本的源码。这里的源码是指android sdk某个版本号（如android-27）的源码。但是在调试的时候，报告源码不匹配，就是说与手机里那一份代码不一样，导致函数的行号对不上。
下面介绍制作一个android-27的源码包方法

## 版本号
查看手机的Build Number，在设置里查看。笔者手机的Build Number是OPM1.171019.016，然后在Google源码官网上比对对应的Branch Name，通过比较发现对应的Branch Name是android-8.1.0_r10。

## 下载源码
```shell
cd android-sdk-source-code
mkdir –p frameworks/base
git clone --depth 1 https://android.googlesource.com/platform/frameworks/base -b android-8.1.0_r10 frameworks/base
git clone --depth 1 https://android.googlesource.com/platform/libcore -b android-8.1.0_r10
git clone --depth 1 https://android.googlesource.com/platform/development -b android-8.1.0_r10
```

## 创建source.properties

```shell
echo -e "Pkg.UserSrc=false\nPkg.Revision=1\nAndroidVersion.ApiLevel=27" > source.properties
```

## 修改脚本
```shell
cat development/build/tools/mk_sources_zip.py | sed -e 's/TOP_FOLDER = .*/TOP_FOLDER = "android-27"/' > my_mk_sources_zip.py
```

## 打包源码android-27-sources.zip

```shell
python my_mk_sources_zip.py -z source.properties android-27-sources.zip
```

## 替换android-sdk并重启Android Studio

```shell
unzip android-27-sources.zip -d ${ANDROID_HOME}/sources
```