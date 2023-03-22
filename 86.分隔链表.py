#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 朴素做法， 找到截断点, 往后找小数据插入截断点之前
        dummy = ListNode(-101)
        dummy.next = head
        pt_cut = dummy
        # 找到截断点
        while pt_cut.next and pt_cut.next.val<x: pt_cut=pt_cut.next
        # 暂存截断点后的节点
        pt_cut_post = pt_cut.next
        # 遍历截断点后的节点, 出现小的则前插
        p = pt_cut.next
        while p and p.next:
            if p.next.val<x:
                # 将当前节点插入到前个节点中
                temp = p.next
                p.next = p.next.next
                pt_cut.next = temp
                pt_cut = temp
            else:
                p = p.next
        pt_cut.next = pt_cut_post

        return dummy.next

# @lc code=end

