#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # dp[i][j]表示i-j是否是一个回文串
        dp = [[0]*len(s) for _ in range(len(s))]

        max_str=''
        max_len=0
        # 单字符串必是回文串
        for i in range(len(s)):
            dp[i][i] = 1
            max_len=1
            max_str=s[i]

        # 层层遍历
        for i in range(1, len(s)):
            for j in range(0, len(s)-i):
                if s[j]==s[j+i] and (i<=1 or dp[j+1][j+i-1]==1):
                    dp[j][j+i]=1
                    if i+1> max_len:
                        max_len=i+1
                        max_str=s[j:j+i+1]


        return max_str
# @lc code=end

