#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        l_b = h-1
        for i in range(h//2):
            for j in range(l_b):
                temp = matrix[i+j+1][i]
                matrix[i+j+1][i] = matrix[h-1-i][1+j+i]
                matrix[h-1-i][i+j+1] = matrix[h-2-i-j][h-1-i]
                matrix[h-2-i-j][h-1-i] = matrix[i][h-2-i-j]
                matrix[i][h-2-i-j] = temp
            l_b = l_b-2
            if l_b<=0:break
# @lc code=end

