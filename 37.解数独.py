#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    row_used   = []   # 当前行已经使用的数字
    col_used   = []   # 当前列已经使用的数字
    block_used = []   # 当前九宫格已经使用的数字
    all_numbers = set([1,2,3,4,5,6,7,8,9])
    numbers = set([c for c in "123456789"])
    def try_solve(self, board, empty_pos)->bool:
        # 没有待填充的位置, 说明已经解完数独
        if len(empty_pos)==0:
            return True
        
        # 获取当前尝试解决的位置
        i, j = empty_pos[0]
        # 获取当前位置所有可以使用的数字
        av_nums_list = Solution.all_numbers\
            -Solution.row_used[i]\
            -Solution.col_used[j]\
            -Solution.block_used[3*(i//3)+j//3]
        # 无可用数字
        if len(av_nums_list)==0: return False
        for num in av_nums_list:
            # 更新占用数字
            board[i][j] = str(num)
            Solution.row_used[i].add(num)
            Solution.col_used[j].add(num)
            Solution.block_used[3*(i//3)+j//3].add(num)
            if self.try_solve(board, empty_pos[1:]):
                return True
            else:
                # 回溯
                Solution.row_used[i].remove(num)
                Solution.col_used[j].remove(num)
                Solution.block_used[3*(i//3)+j//3].remove(num) 
        return False       

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 空出的位置
        empty_pos=[]
        Solution.row_used   = []   # 当前行已经使用的数字
        Solution.col_used   = []   # 当前列已经使用的数字
        Solution.block_used = []   # 当前九宫格已经使用的数字
        # 初始化使用数字
        for i in range(10):
            Solution.row_used.append(set([]))
            Solution.col_used.append(set([]))
            Solution.block_used.append(set([]))
        # 更新已使用数组
        for i in range(9):
            for j in range(9):
                if board[i][j] in Solution.numbers:
                    # pass
                    Solution.row_used[i].add(int(board[i][j]))
                    Solution.col_used[j].add(int(board[i][j]))
                    Solution.block_used[3*(i//3)+j//3].add(int(board[i][j]))
                else:
                    empty_pos.append((i,j))
        
        self.try_solve(board, empty_pos)
# @lc code=end

