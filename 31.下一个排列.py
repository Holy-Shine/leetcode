#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从右往左找到第一个顺序的位置
        pos = len(nums)-1
        while pos:
            if nums[pos-1]<nums[pos]:
                break
            pos-=1
        
        # 旋转 pos~len(nums)-1 区间(该区间必然是逆序的)
        i, j=pos, len(nums)-1
        while i<j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i, j = i+1, j-1
        
        # 交换pos-1位置的值和逆序区间第一个大于该位置的数
        if pos>0:
            for i in range(pos, len(nums)):
                if nums[i]>nums[pos-1]:
                    temp = nums[i]
                    nums[i] = nums[pos-1]
                    nums[pos-1] = temp
                    break
        


            

# @lc code=end

