#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    n2c = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        # 递归出口
        if len(digits)==1:
            return [c for c in Solution.n2c[digits[0]]]
        elif digits!='':
            for c in Solution.n2c[digits[0]]:
                ans.extend([c+x for x in self.letterCombinations(digits[1:])])
        return ans
            
# @lc code=end

