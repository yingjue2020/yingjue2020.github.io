Title: Android ClassLoader
Date: 2019-05-15 10:38:54
Modified: 2019-05-15 10:38:54
Category: Android
Tags: Android, ClassLoader
Slug: android-classloader

# Class
```java
// http://androidxref.com/6.0.1_r10/xref/libcore/libart/src/main/java/java/lang/Class.java
public final class Class<T> implements Serializable, AnnotatedElement, GenericDeclaration, Type {
    static native Class<?> classForName(String className, boolean shouldInitialize,
        ClassLoader classLoader) throws ClassNotFoundException;
}
```
# VMClassLoader
```java
// http://androidxref.com/6.0.1_r10/xref/libcore/libart/src/main/java/java/lang/VMClassLoader.java
package java.lang;
class VMClassLoader{
    native static Class findLoadedClass(ClassLoader cl,String name);
}
```

# BootClassLoader
```java
// http://androidxref.com/6.0.1_r10/xref/libcore/libart/src/main/java/java/lang/ClassLoader.java#762
class BootClassLoader extends ClassLoader{

}
```

# ClassLoader
```java
// http://androidxref.com/6.0.1_r10/xref/libcore/libart/src/main/java/java/lang/ClassLoader.java
public abstract class ClassLoader{

}
```

# BaseDexClassLoader
```java
// http://androidxref.com/6.0.1_r10/xref/libcore/dalvik/src/main/java/dalvik/system/BaseDexClassLoader.java
public class BaseDexClassLoader extends ClassLoader{
    private final DexPathList pathList;

}
```

# DexPathList
```java
// http://androidxref.com/6.0.1_r10/xref/libcore/dalvik/src/main/java/dalvik/system/DexPathList.java
```
