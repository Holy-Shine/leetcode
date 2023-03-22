#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def getGray(self, n: int) -> List[List]:
        if n==1: return [[0],[1]]
        else:
            codes     = self.getGray(n-1)
            new_codes = []
            # 先高位补0, 低位顺序[(0,),(1,)] => [(0,0),(1,0)]
            for code in codes:
                new_codes.append(code+[0])
            for code in codes[::-1]:
                new_codes.append(code+[1])
            return new_codes


    def grayCode(self, n: int) -> List[int]:
        # 我的笨方法, 底层逻辑其实与官方题解一致,只是位操作更加优雅
        # codes = self.getGray(n)
        # ans = []
        # for code in codes:
        #     temp = 0
        #     factor = 1
        #     for x in code:
        #         temp+=(x*factor)
        #         factor*=2
        #     ans.append(temp)
        # return ans
        # 官方题解
        ans = [0]
        for i in range(1, n + 1):
            for j in range(len(ans) - 1, -1, -1):
                ans.append(ans[j] | (1 << (i - 1)))
        return ans


# @lc code=end

