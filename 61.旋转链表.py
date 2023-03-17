#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 链表长度小于等于1
        if not head or not head.next: return head
        # 统计链上有多少节点, 顺便找到尾部节点
        count = 1
        tail = head
        while tail.next: 
            count+=1
            tail=tail.next
        
        k = k%count  # 在该位置截断再拼接链表即可
        p = head
        # 找到截断点位置
        for _ in range(count-1-k): p = p.next
        
        # 再拼接列表
        tail.next = head
        head = p.next
        p.next = None
        return head


# @lc code=end

