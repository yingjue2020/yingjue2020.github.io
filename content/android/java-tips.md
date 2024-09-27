Title: Java 知识点
Date: 2019-05-13 11:06:28
Modified: 2019-05-13 11:06:28
Category: Android
Tags: Java
Slug: java-tips
Figure: java.png

# 可变参数
变长参数是 Java 的一个语法糖，本质上还是基于数组的实现：
```java
void Foo(String... args);
void Foo(String[] args);

// Method signature
([Ljava/lang/String;)V // public void foo(String[] args)
```

注意事项：
- 可变参数只能作为函数的最后一个参数，但其前面可以有也可以没有任何其他参数
- 由于可变参数必须是最后一个参数，所以一个函数最多只能有一个可变参数
- Java的可变参数，会被编译器转型为一个数组

# 关键字 transient
- 一旦变量被transient修饰，变量将不再是对象持久化的一部分，该变量内容在序列化后无法获得访问。
- transient关键字只能修饰变量，而不能修饰方法和类。注意，本地变量是不能被transient关键字修饰的。变量如果是用户自定义类变量，则该类需要实现Serializable接口。
- 被transient关键字修饰的变量不再能被序列化，一个静态变量不管是否被transient修饰，均不能被序列化。

