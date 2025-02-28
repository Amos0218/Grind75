# 給定一棵二叉樹，計算其最大深度。

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            
            # 計算左子樹的深度
            left_depth = depth(node.left)
            # 計算右子樹的深度
            right_depth = depth(node.right)
            # 當前節點的深度 = 左右子樹較大的深度 + 1（加上當前節點）
            return max(left_depth, right_depth) + 1
        
        return depth(root)  # ✅ 這裡要回傳計算結果