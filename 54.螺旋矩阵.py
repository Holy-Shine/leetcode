#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        ct = 0
        right, left, top, bot = n, -1, 0, m
        i, j = -1, -1
        while ct<m*n:
            # 向右
            i, j = i+1, j+1
            while ct<m*n and j<right:
                ans.append(matrix[i][j])
                j, ct = j+1, ct+1
            # 向下
            i, j=i+1, j-1
            while ct<m*n and i<bot:
                ans.append(matrix[i][j])
                i, ct = i+1, ct+1
            # 向左
            i, j=i-1, j-1
            while ct<m*n and j>left:
                ans.append(matrix[i][j])
                j, ct = j-1, ct+1
            # 向上
            i, j=i-1, j+1
            while ct<m*n and i>top:
                ans.append(matrix[i][j])
                i, ct = i-1, ct+1
            # 更新四边
            right, left, top, bot = right-1, left+1, top+1, bot-1
        return ans

# @lc code=end

