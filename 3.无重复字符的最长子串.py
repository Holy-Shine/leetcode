#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_pos = {}
        i,j,ret=0,1,0
        if len(s)>0:
            ch_pos[s[0]]=0
        if len(s)<=1:
            return len(s)
        while j<len(s):
            k=j
            if s[j] in s[i:j]:
                k=j-1
                ret = max(ret, k-i+1)
                i=ch_pos[s[j]]+1
            else:
                ret = max(ret, k-i+1)
            ch_pos[s[j]] = j
            j+=1
        return ret
            
            
        
# @lc code=end

