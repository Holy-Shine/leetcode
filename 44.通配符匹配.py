#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def machTerm(self, s, begin, pat):
        while begin<len(s):
            i = 0
            while begin+i<len(s) and i<len(pat) and (s[begin+i]==pat[i] or pat[i]=='?'):
                i+=1
            if i==len(pat): return True
            begin+=1
        return False

    def isMatch(self, s: str, p: str) -> bool:
        pt_ls = p.split('*')
        # 观察s中是否存在pt_ls的顺序匹配
        begin = 0
        for pt in pt_ls:
            # 尝试匹配列表第一个模式
            while not self.machTerm(s, begin, pt):
                begin+=1
                if begin>len(s): return False
            
            # 已经匹配上一个模式, 索引后移
            begin = begin+len(pt)
        return True

# @lc code=end

