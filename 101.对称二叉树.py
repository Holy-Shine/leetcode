#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equal(self, p, q) -> bool:
        if not p and not q: return True
        if (not p and q) or (not q and p): return False
        return p.val==q.val and \
            self.equal(p.left, q.right) and \
            self.equal(p.right, q.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.equal(root.left,root.right)
# @lc code=end

