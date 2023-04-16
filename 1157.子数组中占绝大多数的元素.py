#
# @lc app=leetcode.cn id=1157 lang=python3
#
# [1157] 子数组中占绝大多数的元素
#

# @lc code=start
class MajorityChecker:
    k = 20

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.loc = defaultdict(list)

        for i, val in enumerate(arr):
            self.loc[val].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        arr_ = self.arr
        loc_ = self.loc
        
        length = right - left + 1
        for i in range(MajorityChecker.k):
            x = arr_[randint(left, right)]
            pos = loc_[x]
            occ = bisect_right(pos, right) - bisect_left(pos, left)
            if occ >= threshold:
                return x
            elif occ * 2 >= length:
                return -1

        return -1



# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# @lc code=end

