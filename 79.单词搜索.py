#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    used = {} # (i,j):1 表示该坐标已经使用过了
    word = ''
    def not_used(self, i,j):
        return (i,j) not in Solution.used or Solution.used[(i,j)]==0
    
    def check(self, board, m, n, i, j, idx) -> bool:
        # 当前待检测字符串为空
        if idx==len(Solution.word): return True
        # 从当前字符的上下左右开始找
        # 上
        if i-1>=0 and self.not_used(i-1,j) and board[i-1][j]==Solution.word[idx]:
            Solution.used[(i-1,j)]=1
            flag = self.check(board, m, n, i-1, j, idx+1)
            Solution.used[(i-1,j)]=0
            if flag: return True
        # 下
        if i+1<m and self.not_used(i+1, j) and board[i+1][j]==Solution.word[idx]:
            Solution.used[(i+1, j)]=1
            flag = self.check(board, m, n, i+1, j, idx+1)
            Solution.used[(i+1, j)]=0
            if flag: return True
        # 左
        if j-1>=0 and self.not_used(i, j-1) and board[i][j-1]==Solution.word[idx]:
            Solution.used[(i, j-1)]=1
            flag = self.check(board, m, n, i, j-1, idx+1)
            Solution.used[(i, j-1)]=0
            if flag: return True
        # 右
        if j+1<n and self.not_used(i, j+1) and board[i][j+1]==Solution.word[idx]:
            Solution.used[(i, j+1)]=1
            flag = self.check(board, m, n, i, j+1, idx+1)
            Solution.used[(i, j+1)]=0
            if flag: return True

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        Solution.used = {}
        Solution.word=word
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    Solution.used[(i,j)]=1
                    flag = self.check(board, m, n, i, j, 1)
                    Solution.used[(i,j)]=0
                    if flag: return True
        return False


# @lc code=end

