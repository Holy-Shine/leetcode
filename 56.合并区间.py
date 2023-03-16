#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 根据左端点进行排序
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        n = len(intervals)

        right = intervals[0][1] # 当前区间覆盖的右端点
        left  = intervals[0][0]
        for i in range(1, n):
            # 找到一个新区间（大于前区间的右端点）
            if intervals[i][0]>right:
                ans.append([left, right])
                left  = intervals[i][0]
            right = max(right, intervals[i][1])
        ans.append([left, right])
        
        return ans


# @lc code=end

