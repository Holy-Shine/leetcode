#
# @lc app=leetcode.cn id=1637 lang=python3
#
# [1637] 两点之间不包含任何点的最宽垂直面积
#

# @lc code=start
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # 根据第一个点排序
        points = sorted(points, key=lambda x: x[0])
        max_width = 0
        for i in range(1, len(points)):
            max_width = max(points[i][0]-points[i-1][0], max_width)

        return max_width


# @lc code=end

