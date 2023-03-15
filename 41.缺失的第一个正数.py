#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # 利用数组下标
        # 遍历数组, 把大于等于1且大小小于数组长的数字放到下标对应的位置
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # 检查数组下标是否一一对应, 不对应则返回那个下标+1
        # 对应, 则返回长度
        for i in range(len(nums)):
            if i+1!=nums[i]:
                return i+1
        return len(nums)+1
# @lc code=end

