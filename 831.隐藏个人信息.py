#
# @lc app=leetcode.cn id=831 lang=python3
#
# [831] 隐藏个人信息
#

# @lc code=start
class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            at_idx = s.find("@")
            return (s[0]+"*****"+s[at_idx-1]+s[at_idx:]).lower()
        nums = ''.join([c for c in s if c in "0123456789" ])
        len_num = len(nums)
        c_type  = len_num-10
        if c_type==0:
            return "***-***-"+nums[-4:]
        if c_type==1:
            return "+*-***-***-"+nums[-4:]
        if c_type==2:
            return "+**-***-***-"+nums[-4:]
        if c_type==3:
            return "+***-***-***-"+nums[-4:]
        


# @lc code=end

