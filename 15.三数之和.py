#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # 排序
        sorted_nums = sorted(nums)
        for i in range(0, len(sorted_nums)-2):
            # 双指针查找
            j=i+1
            k=len(sorted_nums)-1
            tgt = 0-sorted_nums[i]
            while j<k:
                if sorted_nums[j]+sorted_nums[k]==tgt:
                    ans.append((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j+=1
                    k-=1
                elif sorted_nums[j]+sorted_nums[k]<tgt:
                    j+=1
                else:
                    k-=1
        return list(set(ans))
# @lc code=end

