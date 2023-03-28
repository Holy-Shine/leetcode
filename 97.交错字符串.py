#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s2), len(s1)
        if len(s3)!=m+n: return False
        # dp[i][j] 表示 s1[:i+1] 和s2[:j+1] 能否组成s3
        # 本质上就是两个字符串组成的二维矩阵,  从(0,0)开始走到(m,n)
        # 每次只能向右或向下，能否cover s3
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1,n+1): dp[0][i]=(dp[0][i-1] and s1[i-1]==s3[i-1])
        for i in range(1,m+1): dp[i][0]=(dp[i-1][0] and s2[i-1]==s3[i-1])
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j]=(dp[i][j-1] and s1[j-1]==s3[i+j-1]) or (dp[i-1][j] and s2[i-1]==s3[i+j-1])
        
        return dp[m][n]

        

# @lc code=end

