
from typing import List
class Solution:
    def simplifyPath(self, path: str) -> str:
        if path=='/': return '/'
        # 路径栈
        path_stk = ["/"]
        # 去除多斜杠, 并去除尾部斜杠
        new_path = '/'
        pos = 1
        n = len(path)
        prev = '/'
        while pos<n:
            while pos<n and prev=='/' and path[pos]=='/': pos+=1
            if pos<n: 
                new_path+=path[pos]
                prev = path[pos]
                pos+=1
        if len(new_path)>1 and new_path[-1]=='/': new_path = new_path[:-1]
        return new_path


s = Solution()
x=s.simplifyPath("//ffafafa/ffaf////faffa")
print(x)