#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 两次二分搜索
        # 搜索在哪一行
        m, n = len(matrix), len(matrix[0])
        if target<matrix[0][0] or target>matrix[m-1][n-1]: return False
        l, r, mid = 0, m-1, 0
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0]==target: return True
            elif matrix[mid][0]>target: r=mid-1
            elif matrix[mid][0]<target:
                if mid==m-1 or matrix[mid+1][0]>target:break
                if matrix[mid+1][0]==target: return True
                l=mid+1

        # 此时mid为所在行
        l, r, pos = 0, n-1, mid
        while l<=r:
            mid = (l+r)//2
            if matrix[pos][mid]==target: return True
            elif matrix[pos][mid]<target: l=mid+1
            else: r=mid-1
        return False
                
# @lc code=end

