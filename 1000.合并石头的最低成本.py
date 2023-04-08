#
# @lc app=leetcode.cn id=1000 lang=python3
#
# [1000] 合并石头的最低成本
#

# @lc code=start
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):  # 无法合并成一堆
            return -1
        s = list(accumulate(stones, initial=0))  # 前缀和
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int, p: int) -> int:
            if p == 1:  # 合并成一堆
                return 0 if i == j else dfs(i, j, k) + s[j + 1] - s[i]
            return min(dfs(i, m, 1) + dfs(m + 1, j, p - 1) for m in range(i, j, k - 1))
        return dfs(0, n - 1, 1)


# @lc code=end

