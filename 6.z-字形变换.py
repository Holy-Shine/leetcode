#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        step = numRows * 2 - 2
        ret = ''
        for i in range(1, numRows+1):
            # 第一行or最后一行
            j=0
            while step*j+i<=len(s):
                ret+=s[step*j+i-1]
                # 中间行还要考虑第二个字符
                if i>1 and i<numRows:
                    if step*(j+1)-i+2<=len(s):
                        ret+=s[step*(j+1)-i+1]
                j+=1
        return ret
# @lc code=end

