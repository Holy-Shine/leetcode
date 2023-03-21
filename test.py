
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.append(100001) # 哨兵
        n = len(nums)
        cur = 0
        pos = 1
        while pos<n:
            if nums[cur]==nums[pos]:
                # 找到当前第一个不等于cur的位置
                n_same = 1
                while pos<n and nums[pos]==nums[cur]:
                    nums[cur+n_same] = nums[pos]  # 全部搬过来
                    n_same+=1
                    pos+=1
                # 若 n_same 大于1, 说明前一个数字超过两个, 将当前数插入cur+2的位置处
                # 并更新cur
                if n_same>1:
                    nums[cur+2]=nums[pos]
                    cur = cur+(2 if n_same>1 else 1)
            else:
                nums[cur+1]=nums[pos]
                cur+=1
            pos+=1
        return cur


s = Solution()
x=s.removeDuplicates(nums=[0,0,1,1,1,1,2,3,3])
print(x)