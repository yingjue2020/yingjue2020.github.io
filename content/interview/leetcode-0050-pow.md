Title: 【LeetCode 0050】 pow
Date: 2019-05-29 15:06:06
Modified: 2019-05-29 15:06:06
Category: Interview
Tags: Data Structure, Algorithm
Slug: lc-0050-pow
Figure: leetcode.png

# 问题描述
https://leetcode.com/problems/powx-n/

# 代码
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
