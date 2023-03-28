#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = []
    def solve(self, nums: List[int]) -> List[Optional[TreeNode]]:
        # nums 增序排序
        ans = []
        n = len(nums)
        if n==0: return [None]
        if n==1: return [TreeNode(nums[0])]
        for i in range(n):
            # 左子树
            for left_child in self.solve(nums[:i]):
                # 右子树
                for right_child in self.solve(nums[i+1:]):
                    ans.append(TreeNode(
                        val=nums[i],
                        left=left_child,
                        right=right_child
                    ))
        return ans

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.solve([i for i in range(1,n+1)])
        

# @lc code=end

