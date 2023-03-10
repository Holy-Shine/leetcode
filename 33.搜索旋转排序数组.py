#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            # 右半区构成新的旋转数组
            if nums[mid]>=nums[0]:
                if nums[0]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            
            else:
                if nums[mid]<target<=nums[len(nums)-1]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
                
# @lc code=end

