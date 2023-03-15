#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        way = 1

        n = len(height)
        ans = 0
# 解法1, 非优化的动态规划
        # max_l[i] 表示柱子i前面的最高柱子
        # max_r[i] 表示柱子i后面的最高柱子
        max_l, max_r = [0]*n, [0]*n
        for i in range(1, n-1):
            max_l[i] = max(height[i-1], max_l[i-1])
        for i in range(n-2, 0, -1):
            max_r[i] = max(height[i+1], max_r[i+1])
        
        # 遍历柱子, 若当前柱子前的墙比较高, 则累计雨水为(两边较矮的柱子高-当前柱子高)
        for i in range(1, n-1):
            min_wall = min(max_l[i], max_r[i])
            if height[i]<min_wall:
                ans+=(min_wall-height[i])

# 解法2, 单调栈, 具体见https://leetcode.cn/problems/trapping-rain-water/solutions/9112/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/
        return ans

        

# @lc code=end

