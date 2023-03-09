#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:

        way = 2
        ans = ""
        # 方式1, 递归
        if way == 1:
            if n==1: return "1"
            last = self.countAndSay(n-1)
            # 遍历
            cur = 0
            for i in range(1, len(last)+1):
                if i==len(last) or last[i]!=last[cur]:
                    ans+=(str(i-cur)+last[cur])
                    if i!=len(last): cur = i
        # 方式2 递推
        else:
            ans = "1"
            for i in range(1,n):
                # 遍历
                cur = 0
                temp = ''
                for j in range(1, len(ans)+1):
                    if j==len(ans) or ans[j]!=ans[cur]:
                        temp+=(str(j-cur)+ans[cur])
                        if j!=len(ans): cur = j
                ans = temp               
        return ans
# @lc code=end

