#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [[nums[0]]]
        ans = []
        cur = -11
        for i in range(len(nums)):
            if nums[i]!=cur:
                ts = self.permuteUnique(nums[:i]+nums[i+1:])
                ans.extend([[nums[i]]+term for term in ts])
                cur = nums[i]
        # 去重
        ans_set = set([])
        for term in ans:
            ans_set.add(tuple(term))
        return [list(term) for term in ans_set]
# @lc code=end

