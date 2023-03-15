#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#

# @lc code=start
class Solution:
    col_used = []
    ans = 0

    def dag_used(self, pos, cur):
        '''前面每行占用的列的位置
        '''
        for i in range(len(pos)):
            if abs(len(pos)-i)==abs(pos[i]-cur):
                return True
        return False
    def dag_used(self, pos, cur):
        '''前面每行占用的列的位置
        '''
        for i in range(len(pos)):
            if abs(len(pos)-i)==abs(pos[i]-cur):
                return True
        return False
    def dfs(self, r, n: int, pos: List) -> None:
        '''
        r:   当前行标
        pos: 前面已经占用的位置
        '''
        # 检查当前位置是否有可用
        if len(pos)==n:
            Solution.ans+=1
            return
        for i in range(0, n):
            if not Solution.col_used[i] and not self.dag_used(pos, i):
                Solution.col_used[i] = 1
                self.dfs(r+1, n, pos+[i])
                # 回溯
                Solution.col_used[i] = 0
    def totalNQueens(self, n: int) -> int:
        # 初始化列占用
        Solution.col_used = [0]*n
        Solution.ans = 0
        # 从第一行开始依次摆放
        self.dfs(0, n, [])
        return Solution.ans
# @lc code=end

