#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p,q=list1, list2
        if not p: return list2
        if not q: return list1

        # 递归版本
        if p.val<=q.val:
            p.next = self.mergeTwoLists(list1.next, list2)
            return p
        else:
            q.next = self.mergeTwoLists(list1, list2.next)
            return q
        # 非递归版本
        # 确定头指针
        # if p.val<=q.val:
        #     header = p
        #     h = p
        #     p = p.next
        # else:
        #     header = q
        #     h = q
        #     q = q.next

        # while p and q:
        #     if p.val<=q.val:
        #         h.next = p
        #         h = p
        #         p = p.next
        #     else:
        #         h.next = q
        #         h = q
        #         q = q.next
        # if p:
        #     h.next = p
        # if q:
        #     h.next = q
        # return header

# @lc code=end

