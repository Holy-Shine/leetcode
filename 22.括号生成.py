#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        if n==1:
            return ["()"]
        else:
            # 找位置插入
            for s in self.generateParenthesis(n-1):
                for i in range(len(s)+1):
                    ans.append(s[:i]+'()'+s[i:])
            return list(set(ans))


# @lc code=end

