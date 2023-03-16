#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        pos = n-1
        ans = 0
        # 反向找到第一个空格
        while pos>=0 and s[pos]==' ': pos-=1
        while pos>=0 and s[pos]!=' ': 
            ans+=1
            pos-=1
        return ans

# @lc code=end

