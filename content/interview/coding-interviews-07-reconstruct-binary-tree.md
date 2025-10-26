Title: 剑指 Offer 第7题：重建二叉树
Date: 2024-07-07 14:14:29
Modified: 2024-07-07 14:14:29
Category: Interview
Tags: Data Structure, Algorithm
Slug: ci-07-reconstruct-binary-tree
Figure: offer.png
Status: draft

> 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

**C++代码**

```cpp
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        if (pre.size() == 0 || vin.size() == 0) return NULL;
        int val = pre[0];
        TreeNode* root = new TreeNode(val);
        int idx_root = -1;
        for(int idx = 0;idx < vin.size(); idx++){
            if (vin[idx] == val){
                idx_root = idx;
                break;
            }
        }
        int left_node_cnt = idx_root - 0;
        int right_node_cnt = vin.size() - 1 - idx_root;
        if (left_node_cnt != 0){
            vector<int> pre_t(pre.begin()+1,pre.begin()+left_node_cnt+1);
            vector<int> vin_t(vin.begin(),vin.begin()+left_node_cnt);
            root->left = reConstructBinaryTree(pre_t,vin_t);
        }
        if (right_node_cnt != 0){
            vector<int> pre_t(pre.begin()+1+left_node_cnt,pre.end());
            vector<int> vin_t(vin.begin() + idx_root + 1,vin.end());
            root->right = reConstructBinaryTree(pre_t,vin_t);
        }
        return root;
        
    }
};
```