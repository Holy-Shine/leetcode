#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
'''
用一个栈保存所有路径.
根据下一个路径项决定当前出栈还是入栈
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        # if path=='/': return '/'
        # 路径栈
        path_stk = ["/"]
        # 去除多斜杠, 并去除尾部斜杠
        new_path = ''
        pos = 1
        n = len(path)
        prev = '/'
        while pos<n:
            while pos<n and prev=='/' and path[pos]=='/': pos+=1
            if pos<n: 
                new_path+=path[pos]
                prev = path[pos]
                pos+=1
        if len(new_path)>0 and new_path[-1]=='/': new_path = new_path[:-1]

        # 根据斜杠拆分路径
        path_ls = new_path.split('/')
        for p in path_ls:
            # 当前路径, 则无视
            if p=='.': continue
            # 上个路径, 且上个路径不是根路径
            elif p=='..':
                if path_stk[-1]!='/': path_stk.pop()
            else:
                path_stk.append(p)
        return '/'+'/'.join(path_stk[1:])


# @lc code=end

