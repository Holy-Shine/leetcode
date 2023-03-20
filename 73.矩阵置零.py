#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # O(M+N)
        row, col = [0]*m, [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0: row[i], col[j]=1, 1
        for i in range(m):
            for j in range(n):
                if row[i]==1 or col[j]==1: matrix[i][j]=0
# @lc code=end

