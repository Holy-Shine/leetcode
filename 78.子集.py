#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1: return [[nums[0]],[]]
        else:
            # 前一个数组的所有幂集+所有幂集带上当前元素的 总和
            ans = self.subsets(nums[1:])
            l = len(ans)
            for i in range(l):
                ans.append(ans[i]+[nums[0]])
            return ans
# @lc code=end

