#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    SPEC=[0]*4000
    CHAR = [
        ["I", "V", "X"],
        ["X", "L", "C"],
        ["C", "D", "M"],
        ["M"]
    ]
    def __init__(self) -> None:
        Solution.SPEC[4]='IV'
        Solution.SPEC[9]='IX'
        Solution.SPEC[40]='XV'
        Solution.SPEC[90]='XC'
        Solution.SPEC[400]='CD'
        Solution.SPEC[900]='CM'
    def intToRoman(self, num: int) -> str:
        ans = []
        pos=0
        while num:
            # 取1位
            x = num%10
            num = num // 10 
            if x==9:
                ans.append(Solution.CHAR[pos][0]+Solution.CHAR[pos][2])
            elif x==4:
                ans.append(Solution.CHAR[pos][0]+Solution.CHAR[pos][1])
            elif x>5:
                ans.append(Solution.CHAR[pos][1]+(x-5)*Solution.CHAR[pos][0])
            elif x==5:
                ans.append(Solution.CHAR[pos][1])
            elif x>0:
                ans.append(x*Solution.CHAR[pos][0])
            pos+=1
        return ''.join([x for x in ans[::-1]])
                

            

# @lc code=end

