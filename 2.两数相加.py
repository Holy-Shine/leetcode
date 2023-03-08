#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        header = ListNode()
        tail = header
        up=0
        while l1!=None or l2!=None:
            if l1!=None:
                up+=l1.val
                l1=l1.next
            if l2!=None:
                up+=l2.val
                l2=l2.next
            tail.next = ListNode(up%10)
            tail = tail.next
            up = up//10;

        if up!=0:
            tail.next = ListNode(up)
        
        return header.next

            
# @lc code=end

