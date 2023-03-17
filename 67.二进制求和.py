#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 确保a比b长，并旋转a,b
        if len(a)<len(b): 
            temp=a
            a=b
            b=temp
        a, b = a[::-1], b[::-1]
        step = 0
        ans = ''
        # 短部分相加
        for i in range(len(b)):
            temp = int(a[i])+int(b[i])+step
            ans+=str(temp%2)
            step = temp//2
        # 剩余部分
        for i in range(len(b), len(a)):
            temp = int(a[i])+step
            ans+=str(temp%2)
            step = temp//2
        if step: ans+='1'
        return ans[::-1]

        

# @lc code=end

