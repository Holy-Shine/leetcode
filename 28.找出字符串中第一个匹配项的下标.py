#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP
        # 1. 求解next
        nxt = [0]
        now = 0
        x = 1
        while x<len(needle): 
            if needle[x]==needle[now]: 
                now+=1
                x+=1
                nxt.append(now)
            elif now: 
                now = nxt[now-1]
            else:
                x+=1
                nxt.append(0)
        # 2. 比较, p1指向目标串, p2指向模式串
        p1, p2 = 0, 0
        while p1<len(haystack):
            if haystack[p1]==needle[p2]:
                p1,p2 = p1+1, p2+1
            elif p2!=0:
                p2 = nxt[p2-1]
            else:
                p1+=1
            if p2==len(needle):
                return p1-len(needle)
        
        return -1
# @lc code=end

