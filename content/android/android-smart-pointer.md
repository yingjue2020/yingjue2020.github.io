Title: Android 智能指针
Date: 2019-05-24 12:55:08
Modified: 2019-05-24 12:55:08
Category: Android
Tags: Android, SmartPointer
Slug: android-smart-pointer
Figure: android.png

# 相关源码
http://androidxref.com/6.0.1_r10/xref/system/core/include/utils/StrongPointer.h
http://androidxref.com/6.0.1_r10/xref/system/core/include/utils/RefBase.h
http://androidxref.com/6.0.1_r10/xref/system/core/libutils/RefBase.cpp


# StrongPointer

# INITIAL_STRONG_VALUE 为什么不是0
区分从来没有指针引用该对象，还是没有指针引用该对象
如果从来没有调用过，那么mStrong为INITIAL_STRONG_VALUE
如果没有指针引用该对象，mStrong = 0

