#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = [[root]]
        ans = [[root.val]]
        r = True
        while len(q):
            temp  = []
            t_val = []
            for node in q[0]:
                if node.left:
                    temp.append(node.left)
                    t_val.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    t_val.append(node.right.val)
            if len(temp): 
                if r: ans.append(t_val[::-1])
                else: ans.append(t_val)
                q.append(temp)
            q.pop(0)
            r = not r
        return ans
# @lc code=end

