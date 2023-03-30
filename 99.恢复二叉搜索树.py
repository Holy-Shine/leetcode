#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    prev2 = None
    cur = None
    def find(self, root):
        '''中序遍历找异常节点(递增)'''
        if root.left: self.find(root.left)
        if root.val<Solution.prev.val:
            Solution.cur = Solution.prev
            return
        Solution.prev = root
        if root.right: self.find(root.right)

    def change(self, root):
        '''反中序遍历找替换点位(递减)'''
        if root.right: self.change(root.right)
        if root.val>Solution.prev2.val:
            Solution.cur.val, Solution.prev2.val  = Solution.prev2.val, Solution.cur.val
            return
        Solution.prev2 = root
        if root.left: self.change(root.left)       
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 第一趟，找异常位置
        Solution.prev = TreeNode(float("-inf"))
        Solution.prev2 = TreeNode(float("inf")) 
        self.find(root)
        self.change(root)
# @lc code=end

