Title: 剑指 Offer 第5题：替换空格
Date: 2024-07-05 14:11:43
Modified: 2024-07-05 14:11:43
Category: Interview
Tags: Data Structure, Algorithm
Slug: ci-05-replace-space
Figure: offer.png
Authors: Apple
Status: draft

> 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

**示例 1：**
```javascript
//输入：s = "We are happy."
//输出："We%20are%20happy."
```

> 限制：0 <= s 的长度 <= 10000

**思路**

由于字符串是从1个字符替换到3个字符，因此可以创建一个长度为该字符串3倍的字符数组。然后创建一个索引如index为0，index表示遍历完成后的替换字符串的长度，遍历字符串，然后获取字符串的当前字符，判断如果当前字符是空格，则数组的第index为"%",第index + 1为"2",第index + 2为"0",并且将index加3，否则数组的第index项为该字符，并且将index加1，遍历结束后，最后得到的index则为新字符串的长度，从数组的前index个字符中创建新字符串即可。

**C++代码**

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


