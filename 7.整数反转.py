#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2147483648
        MAX_INT = [2,1,4,7,4,8,3,6,4,7]
        if x==MIN_INT:
            return 0
        neg = (x<0)
        temp = -x if neg else x

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
                    return 0
                elif i<MAX_INT[pos]:
                    flg=False
            rst+=i*10**(n-pos-1)
            temp_2=temp_2//10
            pos+=1

        return -rst if neg else rst
        

        


# @lc code=end

