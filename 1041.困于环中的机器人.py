#
# @lc app=leetcode.cn id=1041 lang=python3
#
# [1041] 困于环中的机器人
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cur = [0, 0]  # 当前位置
        d = 0  # 方向 0123 -> 上右下左
        n = len(instructions)
        for i in range(n * 4):
            match instructions[i % n]:
                case 'R': d = (d + 1) % 4  # 右转
                case 'L': d = (d - 1) % 4  # 左转
                case 'G':
                    match d:
                        case 0: cur[1] += 1
                        case 1: cur[0] += 1
                        case 2: cur[1] -= 1
                        case 3: cur[0] -= 1
            if cur == [0, 0] and i % n == n - 1: return True
        return False
# @lc code=end

