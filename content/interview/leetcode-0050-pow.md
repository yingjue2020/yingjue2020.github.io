Title: LeetCode 50 : Pow(x, n)
Date: 2019-05-29 15:06:06
Modified: 2019-05-29 15:06:06
Category: Interview
Tags: Data Structure, Algorithm
Slug: lc-0050-pow
Figure: leetcode.png

> 实现 pow(x, n) ，即计算 $x$ 的整数 $n$ 次幂函数（即，$x^n$ ）。

**示例 1：**

> 输入：x = 2.00000, n = 10

> 输出：1024.00000

**示例 2：**

> 输入：x = 2.10000, n = 3

> 输出：9.26100

**示例 3：**

> 输入：x = 2.00000, n = -2

> 输出：0.25000

> 解释：2-2 = 1/22 = 1/4 = 0.25
 

**提示：**

- -100.0 < x < 100.0
- $-2^{31} <= n <= 2^{31-1}$
- n 是一个整数
- 要么 x 不为零，要么 n > 0 。
- $-10^4 <= x^n <= 10^4$

```go
func myPow(x float64, n int) float64 {
    if (n == 0) {
        return 1.0
    }
    var half float64 = myPow(x,n/2)
    if (n % 2 == 0) {
        return half * half
    }
    if (n > 0) {
        return half * half * x
    }else {
        return half * half / x
    }
}
```

原题：[LeetCode 50](https://leetcode.cn/problems/powx-n/description/)
