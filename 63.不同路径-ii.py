#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        # 初始化行列
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        for i in range(1, m):
            if obstacleGrid[i][0]: dp[i][0] = 0
            else: dp[i][0] = dp[i-1][0]
        for i in range(1, n):
            if obstacleGrid[0][i]: dp[0][i] = 0
            else: dp[0][i] = dp[0][i-1]
        
        # dp过程
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]: dp[i][j] = 0
                else: dp[i][j] = dp[i-1][j]+dp[i][j-1]
        
        return dp[m-1][n-1]

    

# @lc code=end

