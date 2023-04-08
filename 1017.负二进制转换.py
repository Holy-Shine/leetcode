#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#

# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        # 确保余数为0或1
        if n==0: return "0"
        ans = ''
        while n:
            if n>0:
                ans+=str(n%2)
                n = -int((n-1)/2+0.5)
            else:
                ans+=str(((-n)%2))
                n = (-n+1)//2
        return ans[::-1]
# @lc code=end

