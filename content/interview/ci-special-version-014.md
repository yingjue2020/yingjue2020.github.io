Title: 剑指Offer专项突破版第14题：字符串中的变位词
Date: 2024-06-14 14:00
Modified: 2024-06-14 14:00
Category: Interview
Tags: Data Structure, Algorithm
Slug: ci-speical-version-014-check-inclusion
Figure: offer.png
Authors: Apple

> 题目:给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。换句话说，第一个字符串的排列之一是第二个字符串的 子串 。

**示例 1：**

```javascript
// 输入: s1 = "ab" s2 = "eidbaooo"
// 输出: True
// 解释: s2 包含 s1 的排列之一 ("ba").
```

**示例 2：**

```javascript
// 输入: s1= "ab" s2 = "eidboaoo"
// 输出: False
```

**提示:**

- 1 <= s1.length, s2.length <= 10 ^ 4
- s1 和 s2 仅包含小写字母

> 注意：本题与[LeetCode 567 题](https://leetcode.cn/problems/permutation-in-string/description/)相同。

**思路分析**

本题我们可以考虑双指针算法。首先根据题意，对于任意的字符串仅包含小写字母，这也就意味着我们的字符只会包含26个英文字母，根据变位词的定义，我们可以知道如果s2存在一个子字符串，如果它出现的字符数在s1中存在并且相等，那么就意味着s1是s2的变位词。比如根据示例1，从s2中可以找到一个子字符串"ba",恰好"b"和"a"出现的字符数等价于s1出现的字符数，所以s1就是s2的变位词，而对于示例2,s2中就算找到"b"和"a"组成的子字符串，显然也是"boa",而这个字符数明显与s1的字符数不相等，所以也就不是s2的变位词。根据这个性质，我们可以约定一个left和right指针，都是从0开始，首先我们统计s1中出现的字符数，并用一个长度为26的数组存储，当然我们是要对s1中出现的字符数统计为负数，也即对应的字符数自减。我们为什么要这么做？对于双指针区间[left,right],只要存在这个区间的长度等于s1的长度,那么也就意味着存在一个子字符串满足题意。


```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    const n = s1.length,m = s2.length;
    if(n > m){
        return false;
    }
    let letterArr = [];
    for(let i = 0;i <= 26;i++){
        letterArr.push(0);
    }
    for(let i = 0;i < n;i++){
        letterArr[s1[i].charCodeAt() - 'a'.charCodeAt()]--;
    }
    let left = 0;
    for(let right = 0;right < m;right++){
        const char = s2[right].charCodeAt() - "a".charCodeAt();
        letterArr[char]++;
        while(letterArr[char] > 0){
            letterArr[s2[left].charCodeAt() - "a".charCodeAt()]--;
            left++;
        }
        if(right - left + 1 === n){
            return true;
        }
    }
    return false;
};
```

以上算法的时间复杂度和空间复杂度分析如下:

- 时间复杂度O(26 + n + m),也就是O(n + m)。
- 空间复杂度O(1)。