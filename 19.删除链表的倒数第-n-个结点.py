#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 双指针, 1个指针先前进n, 第2个指针再动, 等1指针到尾部, 2指针再删
        first, second = head, head
        for _ in range(n):
            first = first.next
        if first==None: return head.next
        while first.next:
            first=first.next
            second=second.next
        second.next = second.next.next
        
        return head
        
# @lc code=end

