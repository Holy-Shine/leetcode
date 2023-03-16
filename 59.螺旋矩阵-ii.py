#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = []
        num = n*n
        # 初始化矩阵
        for _ in range(n):
            ans.append([0]*n)
        i, j = -1, -1
        ct   = 1
        right, left, top, bot = n, -1, 0, n
        while ct<=num:
            # 向右
            i, j = i+1, j+1
            while ct<=num and j<right:
                ans[i][j] = ct
                j, ct = j+1, ct+1
            # 向下
            i, j=i+1, j-1
            while ct<=num and i<bot:
                ans[i][j] = ct
                i, ct = i+1, ct+1
            # 向左
            i, j=i-1, j-1
            while ct<=num and j>left:
                ans[i][j] = ct
                j, ct = j-1, ct+1
            # 向上
            i, j=i-1, j+1
            while ct<=num and i>top:
                ans[i][j] = ct
                i, ct = i-1, ct+1
            # 更新四边
            right, left, top, bot = right-1, left+1, top+1, bot-1
        return ans
# @lc code=end

