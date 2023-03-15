#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 构建位置-列表字典
        # 11100000000000000000000000代表abc
        pos_list={}
        n = len(strs)
        for i in range(n):
            pos = [0]*26
            # 遍历字符串, 若出现字符, 位置字符串相应位置置为1
            for ch in strs[i]:
                pos[ord(ch)-97]+=1
            pos = tuple(pos)
            if pos not in pos_list:
                pos_list[pos] = []
            pos_list[pos].append(strs[i])
        
        return [ls for ls in pos_list.values()]
# @lc code=end

