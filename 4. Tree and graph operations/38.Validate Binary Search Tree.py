# 判斷其是否是有效的二叉搜尋樹

from typing import Optional  

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min_val, max_val):
            if node == None:
                return True
            # 檢查當前節點是否在範圍內
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # ⭐️遞迴檢查左右子樹
            return (helper(node.left, min_val, node.val) and
                    helper(node.right, node.val, max_val))         
        
        # 初始範圍從 -∞ 到 +∞，逐漸縮小範圍以檢查每個節點
        return helper(root, float('-inf'), float('inf'))  
    

    
##題目重點
# 1.我們檢查一棵樹是否是有效的二元搜尋樹 (BST) 時，
# 不僅要檢查每個節點與其父節點的關係，還要確保該節點的左右子樹也符合 BST 的條件    
# ⭐️:
#   檢查左子樹時，max_val 設定為當前節點的值，這樣左子樹的所有節點必須小於這個值
#   檢查右子樹時，min_val 設定為當前節點的值，這樣右子樹的所有節點必須大於這個值