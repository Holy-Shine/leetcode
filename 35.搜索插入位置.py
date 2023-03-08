#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
            # l越过了 r
            if l>r:
                return l
        

# @lc code=end

