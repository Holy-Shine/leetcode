#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:

        MAX_INT = [2,1,4,7,4,8,3,6,4,7]

        if x<0:
            return False

        temp = x

        # 计算有多少位
        temp_1, n=temp, 0
        while temp_1:
            temp_1=temp_1//10
            n+=1
        
        # 反向累加
        temp_2, pos, rst, flg = temp, 0, 0, True
        while temp_2:
            i = temp_2%10
            # 检查是否越界
            if flg and n==10:
                if i>MAX_INT[pos]:
                    return False
                elif i<MAX_INT[pos]:
                    flg=False
            rst+=i*10**(n-pos-1)
            temp_2=temp_2//10
            pos+=1
        return rst==x
# @lc code=end

