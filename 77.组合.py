#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n<k: return []
        if n==k: return [[i for i in range(1,n+1)]]
        if k==1:
            return [[i] for i in range(1,n+1)]
        else:
            # 从右往左取
            ans = []
            # 取当前末端, 则剩余的n-1里取k-1个数
            for x in self.combine(n-1,k-1): ans.append(x+[n])
            # 不取当前末端, 则剩余的n-1里取 k 个 
            ans.extend(self.combine(n-1, k))
            return ans


# @lc code=end

