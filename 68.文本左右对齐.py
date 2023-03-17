#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        n = len(words)
        cur = 0
        while cur<n:
            line = ''
            # 放入第一个单词
            line+=words[cur]
            # 贪心地拿单词
            next, l_words, l_line = cur+1, len(words[cur]), len(words[cur])
            while next<n and l_line+len(words[next])+1<=maxWidth:
                l_words+=len(words[next])
                l_line +=(len(words[next])+1)
                next+=1
                
            # [cur, next) 为一组单词
            # 不是最后一行
            if next<n:
                # 仅有右侧有空格
                if next-cur==1:
                    line+=(' '*(maxWidth-l_line))
                else:
                    # 计算均匀分配的空格数， 左侧多的空格数
                    n_space = (maxWidth-l_words)//(next-cur-1)
                    m_space = (maxWidth-l_words)%(next-cur-1)
                    for i in range(cur+1, next):
                        if i-cur-1<m_space:
                            line+=(' '*n_space+' '+words[i])
                        else:
                            line+=(' '*n_space+words[i])
            # 最后一行左对齐
            else:
                for i in range(cur+1, n):
                    line+=(' '+words[i])
                line+=(' '*(maxWidth-l_line))
            ans.append(line)
            cur = next
        return ans

# @lc code=end

