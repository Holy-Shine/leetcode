
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    numbers = set([str(i) for i in range(1, 27)])

    def numDecodings(self, s: str) -> int:
        # 递归方法超时
        # Solution.book = [-1]*(len(s)+100)
        # return self.solve(s)
        
        # dp
        dp0, dp1 = 0, 1 if s[0] in Solution.numbers else 0
        n = len(s)
        for i in range(1, n):
            dp0 = dp1
            dp1 = (s[i] in Solution.numbers)*dp1+(s[i-1]+s[i] in Solution.numbers)*dp0
        return dp1


s = Solution()
x=s.numDecodings(s="12")
print(x)