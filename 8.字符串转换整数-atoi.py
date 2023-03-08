#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_INT = -2147483648
        MAX_INT = 2147483647
        str_len = len(s)
        pos=0
        # 忽略前导空格
        while pos<str_len and s[pos]==' ':
            pos+=1

        if pos>=str_len or s[pos] not in "0123456789-+":
            return 0
        neg = s[pos]=='-'
        if s[pos] not in "0123456789":
            pos+=1

        sum = 0
        # 整数逻辑
        while pos<str_len:
            # 跳出逻辑
            if s[pos] not in "0123456789":
                break
            
            # 叠加逻辑
            sum = sum*10+int(s[pos])
            pos+=1
            # 越界逻辑
            if neg and -sum<MIN_INT:
                return MIN_INT
            if not neg and sum>MAX_INT:
                return MAX_INT

        return -sum if neg else sum
            
            
# @lc code=end

