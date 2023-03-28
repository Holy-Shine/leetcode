#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''一趟扫描思路
        找到两个收尾端点：
        1. 两个端点内部修改指针指向
        '''
        dummy = ListNode(0)
        dummy.next = head
        prev_right, right_pos =None, dummy # 旋转后的右侧端点
        for _ in range(left):
            prev_right = right_pos 
            right_pos = right_pos.next
        prev, cur =right_pos, right_pos.next
        for _ in range(right-left):
            next = cur.next # 暂存下一个节点
            cur.next = prev
            prev = cur
            cur = next
        # 此时prev是旋转后的左端点, cur是旋转区间之后的点
        prev_right.next = prev
        right_pos.next = cur

        return dummy.next

        
# @lc code=end

