#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        step = 0
        n = len(digits)
        step = digits[n-1]==9
        digits[n-1] = (digits[n-1]+1)%10
        pos = n-2
        while pos>=0 and step:
            temp_step = digits[pos] == 9
            digits[pos] = (digits[pos]+step)%10
            step = temp_step
            pos-=1
        if step: return [1]+digits
        else: return digits 

            
# @lc code=end

