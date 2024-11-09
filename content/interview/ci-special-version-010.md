Title: 剑指Offer专项突破版第10题：和为k的子数组
Date: 2024-06-10 14:00
Modified: 2024-06-10 14:00
Category: Interview
Tags: Data Structure, Algorithm
Slug: ci-speical-version-010-subarray-sum
Figure: offer.png
Authors: Apple

> 题目:给定一个整数数组和一个整数 k ，请找到该数组中和为 k 的连续子数组的个数。

**示例 1：**

```javascript
// 输入:nums = [1,1,1], k = 2
// 输出: 2
// 解释: 此题 [1,1] 与 [1,1] 为两种不同的情况
```

**示例 2：**

```javascript
// 输入:nums = [1,2,3], k = 3
// 输出: 2
```

**提示:**

- 1 <= nums.length <= 2 * 10 ^ 4
- -1000 <= nums[i] <= 1000
- -10 ^ 7 <= k <= 10 ^ 7

> 注意：本题与[LeetCode 560 题](https://leetcode.cn/problems/subarray-sum-equals-k/description/)相同。

**思路分析**

本题需要用到一个新的算法，叫做前缀和算法，也叫差分算法，所谓的前缀和，意思就是一个数组的某项下标以及某项之前的下标的所有元素的和。前缀和算法有两种，如下图所示:

| | 定义式 | 递推式 |
|:-----:|:-----:|:-----:|
|一维前缀和| $b[i]=\sum_{j=0}^i a[j]$ | $b[i]=b[i-1]+a[i]$ |
|二维前缀和| $b[x][y]=\sum_{i=0}^x\sum_{j=0}^y a[i][j]$ | $b[x][y]=b[x-1][y] + b[x][y-1] - b[x-1][y-1] + b[x][y]$ |


当然在详解前缀和算法之前，先要知道为什么这里不能用滑动窗口算法，因为这里存在负数的情况。现在我们再回到本题，由于存在负数，因此我们可以循环到第i项的时候，计算第i项之前的累加和，然后再减去k，并且用哈希表来存储，如果哈希表中存在这个累加和，就代表一定有符合条件的数组项累加起来等于k，因此我们就可以给结果值加1。详细算法流程如下:

- 初始化前缀和变量以及哈希表。
- 初始化哈希表的初始值即{0 : 1}。
- 计算累加和。
- 将累加和减去k值，然后判断哈希表中是否存在该值，存在则加1，不存在则就等于1，然后将结果值加该哈希表中存储的值。
- 返回结果值。

详情代码如下:

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    // 初始化哈希表和长度
    const map = new Map(),
          len = nums.length;
    //初始化前缀和与结果值
    let sum = 0,res = 0;
    // 初始化哈希表的初始值
    map.set(0,1);
    for(let i = 0;i < len;i++){
        // 计算累加和
        sum += nums[i];
        res += map.get(sum - k) || 0;
        map.set(sum,(map.get(sum) || 0) + 1);
    }
    return res;
};
```

以上算法的时间复杂度和空间复杂度分析如下:

- 时间复杂度O(n)：一轮循环需要n次。
- 空间复杂度O(n):哈希表存储一个元素占用O(1)空间。