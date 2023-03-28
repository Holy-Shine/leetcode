#
# @lc app=leetcode.cn id=1092 lang=python3
#
# [1092] 最短公共超序列
#

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        # dp[i][j] 表示 str1[:i+1]和str2[:j+1]的最长公共子序列长
        dp = [[0]*(n+1) for _ in range(m+1)]
        # path[i][j] 表示str1[:i+1]和str2[:j+1]之间的最长公共子序列的点位
        path = [[[]]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    path[i][j]=path[i-1][j-1]+[(i-1,j-1)]
                else:
                    if dp[i-1][j]>dp[i][j-1]:
                        dp[i][j]=dp[i-1][j]
                        path[i][j]=path[i-1][j]
                    else:
                        dp[i][j]=dp[i][j-1]
                        path[i][j]=path[i][j-1]
        s=''
        prev1, prev2 = 0, 0
        for i, j in path[m][n]:
            s+=str1[prev1:i]+str2[prev2:j]+str1[i]
            prev1, prev2 = i+1, j+1
        s+=str1[prev1:]+str2[prev2:]
        return s
# @lc code=end

