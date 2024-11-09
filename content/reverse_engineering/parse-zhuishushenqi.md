Title: [Android]追书神器：章节内容解密分析
Date: 2020-03-31 10:33:59
Modified: 2020-03-31 10:33:59
Category: Reverse Engineering
Tags: Android App
Slug: parse-zhuishushenqi
Figure: binary.jpg

章节内容解密
```java
package com.ushaqi.zhuishushenqi.reader.txtreader.activity;
public class ReaderNewActivity{
    private void a(FineBookConfigBean bean){

    }
}
```

**示例数据**

```bash
// 章节解密密码
auth.zhuishushenqi.com
productLine=1&
startSeqId=2669&
cp=567b60b6ea95f6ea479a177e&token=tyU2QCjdYHCNyeF8e6476ef1f13b652d13d25d2310eeca5f69e15570325cbac7fd0286494441df9829eb2de8a8b333a98f328b4ba39c4b5475118db133d1742945d11d88087f117c8a4227dce946dd92f13f914076840c97&
bookId=516531015a29ee6a5e0000e1&
chapterNum=1
```
