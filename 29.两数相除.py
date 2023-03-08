#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    MAX_INT=0x7fffffff
    MIN_INT=-2147483648
    def divide(self, dividend: int, divisor: int) -> int:
        # 移位法
        if dividend==0: return 0
        if dividend==Solution.MIN_INT and divisor==-1: return Solution.MAX_INT
        
        neg = (dividend ^ divisor) < 0 # 判断两数是否符号不相同
        
        dividend = abs(dividend)
        divisor  = abs(divisor)
        
        ans = 0
        for i in range(31, -1, -1):
            if (dividend>>i)>=divisor:
                ans+=(1<<i)
                dividend-=(divisor<<i)
        return -ans if neg else ans
    
# @lc code=end

