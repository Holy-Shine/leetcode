#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
from typing import List
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        # 不可能的情况
        if n<k or (n-k)%(k-1)!=0: return -1
        ans = 0
        # 贪心, 每次取和最小的区间聚合
        while len(stones)>=k:
            # 找最小的和
            min_beg = 0
            temp    = sum(stones[0:k])
            min_val = temp
            for i in range(k, len(stones)):
                temp = temp+stones[i]-stones[i-k]
                if temp<min_val:
                    min_val = temp
                    min_beg = i-k+1
            ans+=min_val
            stones = stones[:min_beg]+[min_val]+stones[min_beg+k:]
        return ans
# @lc code=end



s = Solution()
x=s.mergeStones([3,2,4,1],2)
print(x)