#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # dp[i][j]表示到(i,j)的最小路径和
        dp = [[0]*n for _ in range(m)]
        # 初始化第一行第一列
        dp[0][0]=grid[0][0]
        for i in range(1, m): dp[i][0]=dp[i-1][0]+grid[i][0]
        for i in range(1, n): dp[0][i]=dp[0][i-1]+grid[0][i]
        # 遍历
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        
        return dp[m-1][n-1]



# @lc code=end

