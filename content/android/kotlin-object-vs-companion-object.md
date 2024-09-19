---
title: 'Kotlin:object 与 companion object 的区别'
date: 2020-03-16 23:24:33
tags: kotlin
categories: kotlin
---
Title: Kotlin:object 与 companion object 的区别
Date: 2020-03-16 23:24:33
Modified: 2020-03-16 23:24:33
Category: Android
Tags: Kotlin
Slug: kotlin-object-vs-companion-object

## 区别

- object 可以定义在全局也可以在类的内部使用
- object 就是单例模式的化身
- object 可以实现 Java 中的匿名类
- companion object 就是 Java 中的 static 变量
- companion object 只能定义在对应的类中
- object 可以作为变量的定义也可以是表达式
- object 匿名类可以继承并超越 Java 中匿名类而实现多个接口
- object 表达式当场实例化，但定义的 object 变量是延迟实例化的
- object 和 companion object 都可以为其取名也可以隐姓埋名
- object 匿名内部类甚至可以引用并更改局部变量
- companion object 甚至还可以被扩展
- Java 中需要结合 @JvmStatic 和 @JvmField 使用
