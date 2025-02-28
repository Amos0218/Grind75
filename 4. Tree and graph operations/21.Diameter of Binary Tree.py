# 計算一棵二叉樹的直徑。二叉樹的直徑被定義為樹中任意兩個節點之間的最長路徑的長度。
# 這條路徑可以不經過根節點

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 初始化最大直徑
        self.max_diameter = 0
        
        # 深度計算遞歸函數
        def depth(node):
            if not node:
                return 0  # 空節點深度是 0

            # 計算左右子樹的深度
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # 更新最大直徑
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)

            # 返回當前節點的深度，供父節點使用
            return max(left_depth, right_depth) + 1 #加一是因為要把當前節點算進去
        
        # 開始計算
        depth(root)
        return self.max_diameter

##題目重點
# 每個節點的直徑可以看作是「左子樹的深度 + 右子樹的深度」
