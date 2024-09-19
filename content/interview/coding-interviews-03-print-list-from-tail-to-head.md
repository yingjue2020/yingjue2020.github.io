Title: 剑指 Offer 第3题：从尾到头打印链表
Date: 2019-10-17 14:13:21
Modified: 2019-10-17 14:13:21
Category: Interview
Tags: Data Structure, Algorithm
Slug: ci-03-print-list-from-tail-to-head

## 题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
## 思路
解决这个问题肯定需要遍历链表，遍历的顺序是从头到尾的顺序，可输出的顺序却是从尾到头。也就是说第一个遍历到的结点最后一个输出，而最后一个遍历的结点第一个输出。这就是典型的“后进先出”，我们可以用栈实现这种顺序。每经过一个结点的时候，把该结点放到一个栈中，当遍历完整个链表后，再从栈顶开始逐个输出结点的值，此时输出的结点的顺序已经反转过来了。下面的代码采用这种思路实现。

既然用栈实现这个函数，而递归的本质就是一个栈结构，于是很自然地想到使用递归来实现。要实现反过来输出链表，我们每访问到一个结点的时候，先递归输出它后面的结点，再输出该结点自身，这样链表的输出结果就反过来了。但有个问题：但链表非常长的时候，就会导致函数调用的层级很深，从而有可能导致函数调用栈溢出。
## 代码
```cpp
/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> ret;
        stack<int> s;
        ListNode* p = head;
        while(p != NULL){
            int x = p->val;
            p = p->next;
            s.push(x);
        }
        while(s.size() > 0){
            int x = s.top();
            s.pop();
            ret.push_back(x);
        }
        return ret;
    }
};
```