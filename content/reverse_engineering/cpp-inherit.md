Title: C++ 继承
Date: 2019-05-27 09:46:12
Modified: 2019-05-27 09:46:12
Category: Reverse Engineering
Tags: C++, Arm
Slug: cpp-inherit
Figure: cpp.png


```shell
export NDK_ROOT=~/android-ndk-r18b

${NDK_ROOT}/toolchains/llvm/prebuilt/linux-x86_64/bin/clang
  --target=x86_64-none-linux-android
  --gcc-toolchain=${NDK_ROOT}/toolchains/x86_64-4.9/prebuilt/linux-x86_64
  --sysroot=${NDK_ROOT}/sysroot
  -isystem ${NDK_ROOT}/sysroot/usr/include/x86_64-linux-android
  -pie -o  hello.c.o -c hello.c

${NDK_ROOT}/toolchains/llvm/prebuilt/linux-x86_64/bin/clang
  --target=x86_64-none-linux-android
  --gcc-toolchain=${NDK_ROOT}/toolchains/x86_64-4.9/prebuilt/linux-x86_64
  --sysroot  ${NDK_ROOT}/platforms/android-21/arch-x86_64
  -pie hello.c.o -o hello

  ${NDK_ROOT}/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang \
  --target=armv7-none-linux-androideabi \
  --gcc-toolchain=${NDK_ROOT}/toolchains/arm-linux-androideabi-4.9 \
  --sysroot=${NDK_ROOT}/sysroot \
  -isystem ${NDK_ROOT}/sysroot/usr/include/arm-linux-androideabi \
  -pie \
  -o  hello.c.o -c hello.c

${NDK_ROOT}/toolchains/llvm/prebuilt/linux-x86_64/bin/clang
  --target=armv7-none-linux-androideabi
  --gcc-toolchain=${NDK_ROOT}/toolchains/arm-linux-androideabi-4.9/...
  --sysroot  ${NDK_ROOT}/platforms/android-21/arch-arm
  -pie hello.c.o -o hello
```
# 简单多继承
```c++
class A
{
public:
    int m_a;
};

class B:public A{
public:
    int m_b;
};

class C:public A{
public:
    int m_c;
};

class D:public B,public C{
public:
    int m_d;
};

```

clang -cc1 -emit-llvm -fdump-record-layouts -stdlib=libc++ normal_multi_inherit_simple.cpp

```shell
*** Dumping AST Record Layout
         0 | class A
         0 |   int m_a
           | [sizeof=4, dsize=4, align=4,
           |  nvsize=4, nvalign=4]

*** Dumping AST Record Layout
         0 | class B
         0 |   class A (base)
         0 |     int m_a
         4 |   int m_b
           | [sizeof=8, dsize=8, align=4,
           |  nvsize=8, nvalign=4]

*** Dumping AST Record Layout
         0 | class C
         0 |   class A (base)
         0 |     int m_a
         4 |   int m_c
           | [sizeof=8, dsize=8, align=4,
           |  nvsize=8, nvalign=4]

*** Dumping AST Record Layout
         0 | class D
         0 |   class B (base)
         0 |     class A (base)
         0 |       int m_a
         4 |     int m_b
         8 |   class C (base)
         8 |     class A (base)
         8 |       int m_a
        12 |     int m_c
        16 |   int m_d
           | [sizeof=20, dsize=20, align=4,
           |  nvsize=20, nvalign=4]
```

# 带虚函数的多继承

```shell
*** Dumping AST Record Layout
         0 | class A
         0 |   (A vtable pointer)
         8 |   int m_a
           | [sizeof=16, dsize=12, align=8,
           |  nvsize=12, nvalign=8]

*** Dumping AST Record Layout
         0 | class B
         0 |   class A (primary base)
         0 |     (A vtable pointer)
         8 |     int m_a
        12 |   int m_b
           | [sizeof=16, dsize=16, align=8,
           |  nvsize=16, nvalign=8]

*** Dumping AST Record Layout
         0 | class C
         0 |   class A (primary base)
         0 |     (A vtable pointer)
         8 |     int m_a
        12 |   int m_c
           | [sizeof=16, dsize=16, align=8,
           |  nvsize=16, nvalign=8]

*** Dumping AST Record Layout
         0 | class D
         0 |   class B (primary base)
         0 |     class A (primary base)
         0 |       (A vtable pointer)
         8 |       int m_a
        12 |     int m_b
        16 |   class C (base)
        16 |     class A (primary base)
        16 |       (A vtable pointer)
        24 |       int m_a
        28 |     int m_c
        32 |   int m_d
           | [sizeof=40, dsize=36, align=8,
           |  nvsize=36, nvalign=8]
```

# 虚继承
共享虚基类,典型的例子iostream

clang 输出内存布局
```shell
clang -cc1 -fdump-record-layouts -stdlib=libc++ vinherit.cpp
clang -cc1 -emit-llvm -fdump-record-layouts -stdlib=libc++ normal_multi_inherit.cpp
```

```c++
class A
{
public:
    int a;
};

class B:virtual public A{};
class C:virtual public A{};
class D:public B,public C{};

int main(int argc,char* argv[])
{
    D d;
    cout << sizeof(d) << endl;  // 12
    return 0;
}

```

clang++ -cc1 -emit-llvm -fdump-record-layouts -stdlib=libc++ normal_multi_inherit_simple.cpp

_ZTV is a prefix for vtable, 
_ZTS is a prefix for type-string (name)
_ZTI is for type-info.

VTT
virtual thunk to
no-virtual thunk to


typeinfo
vtable pointer = vtable + 0x10 (64bit)

# __imp___cxa_pure_virtual

# destructor
D2 is the "base object destructor". It destroys the object itself, as well as data members and non-virtual base classes.
D1 is the "complete object destructor". It additionally destroys virtual base classes.
D0 is the "deleting object destructor". It does everything the complete object destructor does, plus it calls operator delete to actually free the memory.
