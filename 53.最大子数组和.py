#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 解法1复杂度n
        dp = nums[0]      # 表示包含前一个索引的区间的最大值
        ans = nums[0]  
        for i in range(1, len(nums)):
            dp  = max(dp+nums[i], nums[i])
            ans = max(ans, dp)
        return ans
# @lc code=end

