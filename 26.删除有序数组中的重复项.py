#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        gd = nums[0]
        i=1
        pos=1
        while i<len(nums):
            while i<len(nums) and nums[i]==gd: i+=1
            if i<len(nums):
                gd=nums[i]
                nums[pos]=nums[i]
                pos+=1
                i+=1
        return pos

# @lc code=end

