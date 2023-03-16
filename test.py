
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 
        n = len(nums)
        dp = [0]*n
        dp[n-1] = n-1+nums[n-1] # dp[i] 表示i能够跳的最远的位置
        for i in range(n-2, -1, -1):
            max_pos = 0
            for j in range(i+1, min(n, i+nums[i]+1)):
                max_pos = max(max_pos, dp[j])
            dp[i] = max_pos
        if dp[0]>=n-1: return True
        return False


s = Solution()
s.canJump([1,1,1,0])
print(1)