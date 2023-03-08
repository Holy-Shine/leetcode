#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        # 双指针
        i, j = 0, len(height)-1
        while i<j:
            ans = max(ans, min(height[i], height[j])*(j-i))
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
            
        return ans
            
# @lc code=end

