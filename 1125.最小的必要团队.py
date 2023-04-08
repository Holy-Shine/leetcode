#
# @lc app=leetcode.cn id=1125 lang=python3
#
# [1125] 最小的必要团队
#

# @lc code=start
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # dp[i] 表示满足集合为i的最小需要人的组合，i用位表示
        # 对于新的一个people，若其技能组加入到已有技能组后不存在,
        # 或者加上当前人后，某个技能组可以缩短，则更新那个技能组所需要的最小人
        n = len(req_skills)
        skill_idx = {v:i for i, v in enumerate(req_skills)}
        dp = [None]*(1<<n)
        dp[0] = []
        for i, p in enumerate(people):
            cur_skill = 0
            for s in p: cur_skill |= (1<<skill_idx[s])
            for c in range(1<<n):
                if dp[c]==None: continue   
                comb = c | cur_skill
                if dp[comb]==None or len(dp[c])+1<len(dp[comb]):
                    dp[comb] = dp[c]+[i]
        return dp[(1<<n)-1]

# @lc code=end

