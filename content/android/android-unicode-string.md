---
title: android unicode 字符串
date: 2019-05-24 13:05:38
tags: [android,unicode]
---
Title: Android Unicode 字符串
Date: 2019-05-24 13:05:38
Modified: 2019-05-24 13:05:38
Category: Android
Tags: Android, Unicode
Slug: android-unicode-string

# 相关源码

- [Unicode.h](http://androidxref.com/6.0.1_r10/xref/system/core/include/utils/Unicode.h)
- [Unicode.cpp](http://androidxref.com/6.0.1_r10/xref/system/core/libutils/Unicode.cpp)
- [String8.h](http://androidxref.com/6.0.1_r10/xref/system/core/include/utils/String8.h)
- [String8.cpp](http://androidxref.com/6.0.1_r10/xref/system/core/libutils/String8.cpp)
- [String16.h](http://androidxref.com/6.0.1_r10/xref/system/core/include/utils/String16.h)
- [String16.cpp](http://androidxref.com/6.0.1_r10/xref/system/core/libutils/String16.cpp)
- [SharedBuffer.h](http://androidxref.com/6.0.1_r10/xref/system/core/include/utils/SharedBuffer.h)
- [SharedBuffer.cpp](http://androidxref.com/6.0.1_r10/xref/system/core/libutils/SharedBuffer.cpp)

# String16

```c++
// http://androidxref.com/6.0.1_r10/xref/system/core/libutils/String16.cpp#allocFromUTF8
static char16_t* allocFromUTF8(const char* u8str, size_t u8len)
{
    const ssize_t u16len = utf8_to_utf16_length(u8cur, u8len);
    utf8_to_utf16(u8cur, u8len, u16str);
}

namespace android{

//! This is a string holding UTF-16 characters.
class String16{
private:
    const char16_t*     mString;
}
}
```
