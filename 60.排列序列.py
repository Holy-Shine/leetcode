#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

# @lc code=start
class Solution:
    def way1(self, n: int, k: int) -> str:
        '''方式1, 递归
        '''
        if k==1: return ''.join([str(i) for i in range(1, n+1)])
        if n==1: return "1"
        # 获取前一个排列
        prev = self.way1(n, k-1)
        prev = [ch for ch in prev]  # 变成列表
        # 从右向左找到第一个降序的位置
        pos = n-2
        while pos>=0 and prev[pos]>prev[pos+1]:
            pos-=1
        # 从pos开始, 找到刚好比pos大的那个数的位置
        min_gap = 0x7fffffff
        pos2 = pos+1
        for i in range(pos+1, n):
            if prev[i]>prev[pos] and ord(prev[i])-ord(prev[pos])<min_gap:
                pos2 = i
                min_gap = ord(prev[i])-ord(prev[pos])
        # 交换pos和pos2的字符
        temp = prev[pos2]
        prev[pos2] = prev[pos]
        prev[pos]  = temp

        # 逆序pos后面的字符
        prev[pos+1:] = prev[pos+1:][::-1]
        return ''.join(prev)
    def getPermutation(self, n: int, k: int) -> str:
        # 方式2 循环
        ans = [i for i in range(1, n+1)]
        for i in range(k-1):
            # 从右向左找到第一个降序的位置
            pos = n-2
            while pos>=0 and ans[pos]>ans[pos+1]:
                pos-=1
            # 从pos开始, 找到刚好比pos大的那个数的位置
            min_gap = 0x7fffffff
            pos2 = pos+1
            for i in range(pos+1, n):
                if ans[i]>ans[pos] and ans[i]-ans[pos]<min_gap:
                    pos2 = i
                    min_gap = ans[i]-ans[pos]
            # 交换pos和pos2的数字
            temp = ans[pos2]
            ans[pos2] = ans[pos]
            ans[pos]  = temp

            # 逆序pos后面的字符
            ans[pos+1:] = ans[pos+1:][::-1]

        return ''.join([str(i) for i in ans])
    
                
# @lc code=end

