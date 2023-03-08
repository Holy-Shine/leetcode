#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        pos = 0
        while True:
            if pos>len(strs[0])-1: return ans
            for i in range(1, len(strs)):
                if pos>len(strs[i])-1 or strs[i][pos]!=strs[0][pos]:
                    return ans
            ans+=strs[0][pos]
            pos+=1
        return ans

            
# @lc code=end

