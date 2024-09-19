---
title: 剑指 Offer 第2题：替换空格
date: 2019-10-17 14:11:43
tags: [algorithm,strings]
categories: interview
---
Title: 剑指 Offer 第2题：替换空格
Date: 2019-10-17 14:11:43
Modified: 2019-10-17 14:11:43
Category: Interview
Tags: Data Structure, Algorithm
Slug: ci-02-replace-space

## 题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

## 代码
```cpp
class Solution {
public:
	void replaceSpace(char *str,int length) {
        if (str == NULL) return;
        if (length <= 0) return;
        int spaceCount = 0;
        int i = 0;
        while(str[i] != '\0'){
            if (str[i] == ' ') spaceCount++;
            i++;
        }
        if (spaceCount == 0) return;
        
        int originLength = i;
        int newLength = i + spaceCount * 2;
        i = originLength - 1;
        int j = newLength - 1;
        str[j+1] = '\0';
        while(i >= 0){
            if (str[i] == ' '){
                str[j] = '0';
                str[j-1] = '2';
                str[j-2] = '%';
                j -= 3;
                i--;
            }else{
                str[j] = str[i];
                i--;
                j--;
            }
        }
	}
};
```

## 思路
