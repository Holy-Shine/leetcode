#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        p, q, cur = head, head.next, head.val
        while p:
            while q and q.val==cur:
                q = q.next
            p.next = q
            if q: cur = q.val
            p = q
            if p: q = p.next
        return head

# @lc code=end

