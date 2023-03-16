#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#





# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 
        n = len(nums)
        dp = nums[0] # dp表示最远右端点位置
        if len(nums)==1: return True
        # 从1开始
        pos = 1
        while pos<n and pos<=dp:
            dp = max(dp, min(n-1, pos+nums[pos]))
            pos+=1
        
        return dp>=n-1

# @lc code=end

