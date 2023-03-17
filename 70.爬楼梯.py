#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 斐波那契数列
        a, b = 1, 2
        if n==1: return 1
        if n==2: return 2
        for _ in range(2,n):
            a, b = b, a+b
        return b
# @lc code=end

