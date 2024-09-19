Title: 剑指 Offer 第1题：二维数组中的查找
Date: 2019-10-15 14:18:25
Modified: 2019-10-15 14:18:25
Category: Interview
Tags: Data Structure, Algorithm
Slug: ci-01-find-in-2d-array

# 题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 代码
```c++
class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        int m = array.size();
        if (m == 0) return false;
        int n = array[0].size();
        int i = m - 1;
        int j = 0;
        while(i >= 0 && j < n){
            if (array[i][j] > target){
                i--;
            }else if (array[i][j] < target){
                j++;
            }else{
                return true;
            }
        }
        return false;
    }
};
```
# 思路
利用二维数组由上到下，由左到右递增的规律，选取左下角的元素a[i][j]与target进行比较，当target小于元素a[i][j]时，那么target必定在元素a所在行的上边,即i--；当target大于元素a[i][j]时，那么target必定在元素a所在列的右边,即j++；选取右上角的元素a[i][j]与target进行比较，当target小于元素a[i][j]时，那么target必定在元素a所在列的左边,即j--；当target大于元素a[i][j]时，那么target必定在元素a所在行的下边,即i++。演示代码选取左下角元素编写。
