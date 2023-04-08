#
# @lc app=leetcode.cn id=1053 lang=python3
#
# [1053] 交换一次的先前排列
#

# @lc code=start
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        gd = n-1
        # 单调递减栈
        stk = [gd]
        for i in range(n-2, -1,-1):
            if arr[i]<=arr[stk[-1]]: stk.append(i)
            # 找最后一个比当前数小的替换
            else:
                idx = 0
                while idx<len(stk) and arr[stk[idx]]>=arr[i]: idx+=1
                while idx+1<len(stk) and arr[stk[idx+1]]==arr[stk[idx]]: idx+=1
                if idx<len(stk):
                    arr[stk[idx]], arr[i] = arr[i], arr[stk[idx]]
                    return arr

        return arr

# @lc code=end

