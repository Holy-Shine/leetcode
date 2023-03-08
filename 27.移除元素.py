#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        i=0
        while i<len(nums):
            while i<len(nums) and nums[i]==val: i+=1
            if i<len(nums):
                nums[pos]=nums[i]
                pos+=1
                i+=1
        return pos

# @lc code=end

