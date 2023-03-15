#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] 表示跳到i至少需要多少步
        dp = [0x7fffffff]*n
        dp[0] = 0
        for i in range(n-1):
            cur_jump_len = nums[i] # 当前的跳跃步长
            for j in range(i+1, min(n, i+cur_jump_len+1)):
                dp[j] = min(dp[j], dp[i]+1)
        return dp[n-1]



# @lc code=end

