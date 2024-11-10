Title: 剑指 Offer 第10题：斐波那契数列
Date: 2024-07-10 14:31:55
Modified: 2024-07-10 14:31:55
Category: Interview
Tags: Data Structure, Algorithm
Slug: ci-10-fibonacci
Figure: offer.png

> 题目:写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：。

```javascript
//F(0) = 0,   F(1) = 1
//F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
```
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

**示例 1：**

```javascript
//输入：n = 2
//输出：1
```

**示例 2：**

```javascript
//输入：n = 5
//输出：5
```
**提示：**

- 0 <= n <= 100

**思路分析**

在解答本题之前，我们通过题意也已经理解到了斐波那契数列，即f(n + 1) = f(n) + f(n - 1)。也因此我们可以通过递归就可以解决本题。但实际上递归法在本题是最烂的解法，这是因为无脑递归会让我们做很多重复的遍历工作，导致时间复杂度增大，显然不是我们想要的结果。

方法一：递归法

```javascript
var fib = function(n) {
    if(n <= 2){
        return n === 0 ? 0 : 1;
    }else{
        return (fib(n - 1) + fib(n - 2)) % 1000000007;
    }
};
```

以上算法的时间复杂度和空间复杂度分析如下:

- 时间复杂度：O(2 ^ n)。
- 空间复杂度：O(n)。

递归法

方法二：动态规划

动态规划解析：

- 状态定义： 设arr为一维数组，其中 arr[i] 的值代表斐波那契数列第i个数字 。
- 转移方程： arr[i + 1] = arr[i] + arr[i - 1] ，即对应数列定义 f(n + 1) = f(n) + f(n - 1)；
- 初始状态： arr[0] = 0, arr[1] = 1 ，即初始化前两个数字；
- 返回值： arr[n] ，即斐波那契数列的第 n 个数字。
- 空间复杂度优化：

若新建长度为n的arr列表，则空间复杂度为O(N)。

由于 arr 列表第 i 项只与第 i-1 和第 i-2 项有关，因此只需要初始化三个整形变量 sum, a, b ，利用辅助变量 sum 使 a, b两数字交替前进即可 （具体实现见代码） 。

节省了 arr 列表空间，因此空间复杂度降至 O(1) 。如下图所示:


```javascript
/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    let a = 0,b = 1,sum;
    for(let i = 0;i < n;i++){
        sum = (a + b) % 1000000007;
        a = b;
        b = sum;
    }
    return a;
};
```

以上算法的时间复杂度和空间复杂度分析如下:

- 时间复杂度：O(n), 计算 f(n)需循环 n 次，每轮循环内计算操作使用 O(1) 。
- 空间复杂度：O(1), 几个标志变量使用常数大小的额外空间。

[更多思路](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/mian-shi-ti-10-i-fei-bo-na-qi-shu-lie-dong-tai-gui/)。