#
# @lc app=leetcode.cn id=1641 lang=python3
#
# [1641] 统计字典序元音字符串的数目
#

# @lc code=start
class Solution:

    @cache
    def solve(self, n: int, idx: int) -> int:
        if n==1: return 5-idx
        ans = 0
        for i in range(idx, 5):
            ans+=self.solve(n-1, i)
        return ans
    def countVowelStrings(self, n: int) -> int:
        return self.solve(n, 0)

# @lc code=end

