#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
'''
递归(超时)
f(s)=(1/0)*f(s[1:])+(1/0)*f(s[2:])
主要看s[0]和s[:2]在不在数字集合里

dp
dp[i]: 以字符 i 结尾的解析总数
 dp[i] = dp[i-1]*flag1+dp[i-2]*flag2 
 flag1: 当前字符是否可以单独解码, 0就不可以
 flag2: 当前字符是否可以跟前一个字符一起解码, 10-26以外的都不可以

'''
class Solution:
    numbers = set([str(i) for i in range(1, 27)])
    book = []
    def solve(self, s) -> int:
        l = len(s)
        if Solution.book[l]!=-1: return Solution.book[l]
        if l==1: return (s in Solution.numbers)*1
        if l==2: return (s in Solution.numbers)*1+(s[0] in Solution.numbers and s[1] in Solution.numbers)*1
        else:
            Solution.book[l] = (s[0] in Solution.numbers)*self.numDecodings(s[1:])+\
                   (s[:2] in Solution.numbers)*self.numDecodings(s[2:])
            return Solution.book[l]
    def numDecodings(self, s: str) -> int:
        # 递归方法超时
        # Solution.book = [-1]*(len(s)+100)
        # return self.solve(s)
        
        # dp
        dp0, dp1 = 1, 1 if s[0] in Solution.numbers else 0
        n = len(s)
        for i in range(1, n):
            temp = dp1
            dp1 = (s[i] in Solution.numbers)*dp1+(s[i-1]+s[i] in Solution.numbers)*dp0
            dp0 = temp
        return dp1


        



# @lc code=end

