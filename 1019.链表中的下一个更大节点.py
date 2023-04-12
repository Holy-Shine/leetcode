#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # 单调递减栈，当前数大于栈顶，则依次出栈，最后栈里剩的元素就是不存在大的
        stk = [(0,head.val)]# 存下标和值
        ans = [0]
        p = head.next
        while p:
            while stk and p.val>stk[-1][1]:
                ans[stk.pop()[0]] = p.val
            stk.append((len(ans), p.val))
            ans.append(0) # 占位
            p = p.next
        return ans

        



# @lc code=end

