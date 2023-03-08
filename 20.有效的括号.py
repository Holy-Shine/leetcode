#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    pairs = {")":"(", "}":"{","]":"["}
    def isValid(self, s: str) -> bool:
        ss = []
        for c in s:
            if len(ss)>0 and c in Solution.pairs and ss[-1]==Solution.pairs[c]:
                ss.pop()
            else:
                ss.append(c)
        
        return len(ss)==0
# @lc code=end

