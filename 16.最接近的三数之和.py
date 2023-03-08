#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 0
        min_dis = 0x7fffffff
        nums = sorted(nums)
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j<k:
                all = nums[i]+nums[j]+nums[k]
                if all>target:
                    k-=1
                if all<target:
                    j+=1
                if all==target:
                    return all
                if abs(all-target)<min_dis:
                    min_dis = abs(all-target)
                    ans = all
        return ans
# @lc code=end

