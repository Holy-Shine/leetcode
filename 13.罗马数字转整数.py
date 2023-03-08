#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        p={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l = 0
        for i in range(0, len(s)-1):
            if p[s[i]] >= p[s[i + 1]]:
                l += p[s[i]]
            else:
                l -= p[s[i]]
        l+=p[s[-1]]
        return l
# @lc code=end

