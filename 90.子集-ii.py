#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)

        ans = [[]]
        prev_len = 0
        cur      = -100
        # 总的逻辑跟题目 子集 一样, 都是对于新的元素, 每次都加入到前一个元素的子集中, 形成新的子集 
        # 区别是, 对于同样的元素，排除已经加过的情况, 也就是说, 重复的元素只扩展其上一个相同的元素扩展的那部分子集
        for i in range(0, n):
            len_ans = len(ans)
            if nums[i]==cur:
                for j in range(prev_len, len_ans):
                    ans.append(ans[j]+[cur])
            else:
                for j in range(len_ans):
                    ans.append(ans[j]+[nums[i]])
                    cur = nums[i]
            prev_len = len_ans
        return ans



            
# @lc code=end

