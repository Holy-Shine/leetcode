#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = [[root]]
        ans = [[root.val]]
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
                ans.append(t_val)
                q.append(temp)
            q.pop(0)
        return ans
# @lc code=end

