#
# @lc app=leetcode.cn id=1147 lang=python3
#
# [1147] 段式回文
#

# @lc code=start
class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        b, e = 0, n
        l = 1
        r = n-l
        ans = 0
        while l<=r:
            if text[b:l]==text[r:e]:
                b, e = l, r
                ans+=2
                if l==r: break
            l+=1
            r-=1
        if l>r: ans+=1 
        return ans


# @lc code=end

