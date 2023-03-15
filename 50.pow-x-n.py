#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        举例：
        x^31=>
            x^15*x^15*x => x^15 =>
            x^7*x^7*x => x^7 =>
            x^3*x^3*x => x^3 =>
            x*x*x
        '''
        if n==0: return 1
        sum = x
        # 求出2分列表, 例如: 31=>(15,1)=>(7,1)=>(3,1)=>(1,1)
        two_list = []
        temp_x = abs(n)
        while temp_x!=1:
            two_list.append(temp_x%2)
            temp_x = temp_x //2
        
        # 逆序二分列表，累乘
        for ad in two_list[::-1]:
            sum = sum*sum*x if ad else sum*sum

        return sum if n>0 else 1/sum
# @lc code=end

