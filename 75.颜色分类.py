#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_0, num_1 = 0,0
        for num in nums:
            if num==0: num_0+=1
            if num==1: num_1+=1
        for i in range(len(nums)):
            if i<num_0: nums[i]=0
            elif i<num_1+num_0: nums[i]=1
            else: nums[i]=2
# @lc code=end

