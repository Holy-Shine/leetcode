#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = [0] 
        if num1=='0' or num2=='0': return "0"
        # 被乘数取短的那个
        if len(num1)<len(num2): 
            temp = num1
            num1=num2
            num2 = temp
        # 被乘数从个位开始算起
        for i,ch in enumerate(num2[::-1]):
            ans_temp = []
            f1 = int(ch)
            # 和乘数做乘法, 计算中间结果
            step = 0 # 乘法进位
            for c in num1[::-1]:
                f2   = int(c)
                rs   = (f1*f2+step)%10
                step = (f1*f2+step)//10
                ans_temp.append(rs)
            if step: ans_temp.append(step)
            # 累加ans_temp和ans
            step = 0 # 加法进位
            for j in range(len(ans_temp)):
                if i+j<len(ans):
                    add_rst  = ans[i+j]+ans_temp[j]+step
                    step     = add_rst//10
                    ans[i+j] = add_rst%10
                else:
                    add_rst  = ans_temp[j]+step
                    step = add_rst//10
                    ans.append(add_rst%10)
            if step: ans.append(step)

        return ''.join(str(x) for x in ans[::-1])
    



# @lc code=end

