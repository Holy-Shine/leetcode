#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)-3):
            # 三数和
            for j in range(i+1, len(nums)-2):
                k, l =j+1, len(nums)-1
                while k<l:
                    all = nums[i]+nums[j]+nums[k]+nums[l]
                    if all==target:
                        ans.append((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif all<target:
                        k+=1
                    else:
                        l-=1
        
        return list(set(ans))
# @lc code=end

