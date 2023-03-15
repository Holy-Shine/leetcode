#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        # 候选集已经不存在比target小的, 或者已经没有候选集
        flag = False
        for can in candidates:
            if target>=can:
                flag = True
                break
        if not flag:
            return []
        
        ans = []
        # 取当前数
        if target - candidates[0] == 0:
            return [[target]]
        else:
            # 取完当前数还有数
            ans.extend(self.combinationSum(candidates, target-candidates[0]))
            ans.extend(self.combinationSum(candidates[1:],target-candidates[0]))
            for ls in ans:
                ls.append(candidates[0])
            # 不取当前数
            ans.extend(self.combinationSum(candidates[1:], target))
            
            # 去重
            return [list(a) for a in set([tuple(t) for t in ans])]
        



# @lc code=end

