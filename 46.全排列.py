#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [[nums[0]]]
        ans = []
        for i in range(len(nums)):
            ts = self.permute(nums[:i]+nums[i+1:])
            ans.extend([[nums[i]]+term for term in ts])
        return ans
# @lc code=end

