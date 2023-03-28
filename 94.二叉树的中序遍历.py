#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        # 递归
        # if root:
        #     ans+=self.inorderTraversal(root.left)
        #     ans.append(root.val)
        #     ans+=self.inorderTraversal(root.right)

        # 迭代, 栈
        if root:
            stk = [[root, False, False]]
            while len(stk):
                top = stk[-1]
                # 看栈顶有没有左子树
                if top[0].left and not top[1]:
                    stk.append([top[0].left, False, False])
                    top[1]=True # 左子树已遍历过
                else:
                    ans.append(top[0].val)
                    stk.pop()
                    # 如果有右子树
                    if top[0].right and not top[2]: 
                        stk.append([top[0].right,False, False])
                        top[2] = True
        
        return ans
# @lc code=end

