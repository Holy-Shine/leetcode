#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    numbers = set([c for c in "123456789"])
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 未使用数组
        row_used   = []   # 当前行已经使用的数字次数
        col_used   = []   # 当前列已经使用的数字次数
        block_used = []   # 当前九宫格已经使用的数字次数
        # 初始化次数数组
        for i in range(10):
            row_used.append([0]*10)
            col_used.append([0]*10)
            block_used.append([0]*10)
        # 更新未使用数组
        for i in range(9):
            for j in range(9):
                if board[i][j] in Solution.numbers:
                    # pass
                    row_used[i][int(board[i][j])] += 1
                    col_used[j][int(board[i][j])] += 1
                    block_used[3*(i//3)+j//3][int(board[i][j])] += 1
        
        # 检查当前数字是否用了两次
        for i in range(10):
            for j in range(10):
                if row_used[i][j]>1 or col_used[i][j]>1 or block_used[i][j]>1:
                    return False
        return True
# @lc code=end

