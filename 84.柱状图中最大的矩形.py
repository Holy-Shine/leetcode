#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

'''
单调栈：
在一维数组中对每一个数找到第一个比自己小的元素。
这类“在一维数组中找第一个满足某种条件的数”的场景就是典型的单调栈应用场景。
'''

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
# @lc code=end

