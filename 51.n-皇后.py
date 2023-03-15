#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    col_used = []
    ans = []

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
            Solution.ans.append(pos)
            return
        for i in range(0, n):
            if not Solution.col_used[i] and not self.dag_used(pos, i):
                Solution.col_used[i] = 1
                self.dfs(r+1, n, pos+[i])
                # 回溯
                Solution.col_used[i] = 0

        
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 初始化列占用和斜对角占用
        Solution.col_used = [0]*n
        Solution.ans = []
        # 从第一行开始依次摆放
        self.dfs(0, n, [])
        ans = []
        for a in Solution.ans:
            ss = []
            for pos in a:
                ss.append('.'*pos+'Q'+'.'*(n-pos-1))
            ans.append(ss)
        return ans
# @lc code=end

