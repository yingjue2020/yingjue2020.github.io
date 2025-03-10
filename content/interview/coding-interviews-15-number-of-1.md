Title: 剑指 Offer 第15题：二进制中1的个数
Date: 2024-07-15 14:34:11
Modified: 2024-07-15 14:34:11
Category: Interview
Tags: Data Structure, Algorithm
Slug: ci-15-number-of-1
Figure: offer.png

> 题目:请实现一个函数，输入一个整数（以二进制串形式），输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

**示例 1：**

```javascript
// 输入：00000000000000000000000000001011
// 输出：3
// 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
```

**示例 2：**

```javascript
// 输入：00000000000000000000000010000000
// 输出：1
// 解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
```

**示例 3：**

```javascript
// 输入：11111111111111111111111111111101
// 输出：31
// 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
```

> 提示：输入必须是长度为 32 的 二进制串 。

**思路分析**

本题用原生api方法或者正则表达式都可以解决，也可以用位操作符来解决。


方法一:api方法

```javascript
var hammingWeight = function (n) {
    return n.toString(2).split("0").join("").length;
};
```

以上算法的时间复杂度和空间复杂度分析如下:

- 时间复杂度：O(1)。
- 空间复杂度：O(1)。

方法二:正则表达式

```javascript
var hammingWeight = function (n) {
    let match_arr = n.toString(2).match(/1/g);
    return match_arr ? match_arr.length : 0;
};
```

以上算法的时间复杂度和空间复杂度分析如下:

- 时间复杂度：O(1)。
- 空间复杂度：O(1)。

方法二:位操作符

```javascript
var hammingWeight = function (n) {
    let count = 0;
    while(n !== 0){
        // 按位与操作符见https://segmentfault.com/a/1190000018241410这篇文章
        n = n & (n - 1);
        count++;
    }
    return count;
};
```

以上算法的时间复杂度和空间复杂度分析如下:

- 时间复杂度：O(logn),循环次数等于 n 的二进制位中 1 的个数，最坏情况下 n 的二进制位全部为 1。我们需要循环 logn 次。
- 空间复杂度：O(1)。

[更多思路](https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/er-jin-zhi-zhong-1de-ge-shu-by-leetcode-50bb1/)。