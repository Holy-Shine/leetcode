#
# @lc app=leetcode.cn id=2367 lang=python3
#
# [2367] 算术三元组的数目
#

# @lc code=start
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        nums = set(nums)
        for num in nums:
            if num-diff in nums and diff+num in nums:
                ans+=1
        return ans
# @lc code=end

