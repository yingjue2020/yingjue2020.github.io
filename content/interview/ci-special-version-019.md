Title: 剑指Offer专项突破版第19题：最多删除一个字符得到回文
Date: 2024-06-19 14:00
Modified: 2024-06-19 14:00
Category: Interview
Tags: Data Structure, Algorithm
Slug: ci-speical-version-019-valid-palindrome
Figure: offer.png
Authors: Apple
Status: draft

> 题目:给定一个非空字符串 s，请判断如果 最多 从字符串中删除一个字符能否得到一个回文字符串。

**示例 1：**

```javascript
// 输入: s = "aba"
// 输出: true
```

**示例 2：**

```javascript
// 输入: s = "abca"
// 输出: true
// 解释: 可以删除 "c" 字符 或者 "b" 字符
```

**示例 3：**

```javascript
// 输入: s = "abc"
// 输出: false
```

**提示:**

- 1 <= s.length <= 2 * 10 ^ 5
- s 由小写英文字母组成

> 注意：本题与[LeetCode 680 题](https://leetcode.cn/problems/valid-palindrome-ii/description/)相同。

**思路分析**

本题思路和有效的回文很相似，我们可以定义2个指针left和right，然后判断两边字符（s[left] === s[right]）是否相等，如果不相等，再比较是去除左边一个字符即left指针加1是否和右边字符相等（s[left + 1] === s[right]）或者去除右边一个字符，即right指针减1（s[left] === s[right - 1]）。代码如下:

```javascript
var isPalindrome = function(s,start,end){
    while(start < end){
        if(s[start] !== s[end]){
            return false;
        }
        start++;
        end--;
    }
    return true;
}
/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function(s) {
    let len = s.length,left = 0,right = len - 1;
    while(left < right){
        if(s[left] !== s[right]){
            return isPalindrome(s,left + 1,right) || isPalindrome(s,left,right - 1);
        }
        left++;
        right--;
    }
    return true;
};
```

以上算法的时间复杂度和空间复杂度分析如下:

- 时间复杂度：O(n * m)。
- 空间复杂度：O(1)。