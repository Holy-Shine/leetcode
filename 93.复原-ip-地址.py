#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    ips = []
    def solve(self, s, ls: List[int]) -> None:
        l = len(ls)  # 当前ip已经有l个了
        # 剩余长度不足, 则直接返回
        if 4-l>len(s): return
        if len(ls)==3:
            # 非前导零且符合规范, 则找到一组解
            if str(int(s))==s and 0<=int(s)<=255:
                Solution.ips.append(ls+[int(s)])
        else:
            # 看前3位, 2位, 1位
            if len(s)>=1:
                self.solve(s[1:], ls+[int(s[0])])
            if len(s)>=2 and str(int(s[:2]))==s[:2]:
                self.solve(s[2:], ls+[int(s[:2])])
            if len(s)>=3 and str(int(s[:3]))==s[:3] and 0<=int(s[:3])<=255:
                self.solve(s[3:], ls+[int(s[:3])])

    def restoreIpAddresses(self, s: str) -> List[str]:
        Solution.ips = []
        self.solve(s, [])

        return ['.'.join([str(i) for i in ip]) for ip in Solution.ips]
# @lc code=end

