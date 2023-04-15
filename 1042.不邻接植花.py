#
# @lc app=leetcode.cn id=1042 lang=python3
#
# [1042] 不邻接植花
#

# @lc code=start
class Solution:
    ans = None
    flag = False
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # dfs， 类似8皇后
        # 构建邻居矩阵 [[2,3,4],[3,4,5]]
        p_neighbors =[[] for _ in range(0, n+1)]
        for path in paths:
            p_neighbors[path[0]].append(path[1])
            p_neighbors[path[1]].append(path[0])  # 节点双向

        # pos_flag[i] 表示花园i的占用情况, 1,2,4,8分别表示已经使用了花1,2,3,4
        pos_flag = [0]*(n+1)
        checker = [1,2,4,8] # 检查器
        Solution.flag = False #　全局检查器
        def solve(n_p):
            # 表示已经处理完N个节点
            if Solution.flag: return
            if n_p==n+1: 
                Solution.ans=[i for i in pos_flag]
                Solution.flag = True
                return
            # 检查当前节点的邻居占用情况
            ocpy = sum(set([pos_flag[i] for i in p_neighbors[n_p]]))
            for ck in checker:
                # 未占用
                if ck & ocpy == 0:
                    pos_flag[n_p]=ck # 更新占用
                    solve(n_p+1)
                    pos_flag[n_p]=0 # 回溯
        
        solve(1) # 从节点1开始处理
        return [checker.index(x)+1 for x in Solution.ans[1:]]


# @lc code=end

