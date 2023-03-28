#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        # 卡特兰数
        if n==0: return 0
        dp = [0]*(n+1)
        dp[0], dp[1] = 1,1
        for i in range(2, n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-j-1]
        return dp[-1]
# @lc code=end

