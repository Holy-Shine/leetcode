#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
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
        myhead = ListNode(101)
        myhead.next = head
        # 快慢指针
        prev, p_slow, p_fast = myhead, head, head
    
        while p_fast:
            n_same = 0
            while p_fast and p_fast.val==p_slow.val:
                p_fast = p_fast.next
                n_same+=1
            if n_same==1:
                prev.next = p_slow
                prev = p_slow
            elif p_fast==None:
                prev.next = None
            p_slow = p_fast
        return myhead.next
            


# @lc code=end

