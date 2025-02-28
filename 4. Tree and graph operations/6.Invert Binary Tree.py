# 給定一個二元樹，請將其左右子樹反轉，即顛倒整個二元樹

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 基本情況：如果樹是空的，返回空
        if not root:
            return None
        
        # 交換當前節點的左右子樹
        root.left, root.right = root.right, root.left
        
        # 遞迴處理左右子樹
        self.invertTree(root.left)   #交換左子樹的左右子樹
        self.invertTree(root.right)  #交換右子樹的左右子樹
        
        # 返回反轉後的根節點
        return root

##題目重點
# 1.這個 Optional[TreeNode] 是告訴 Python，root 這個變數可以是 TreeNode 類型，
# 也可以是 None（也就是根本沒有節點，樹是空的） 
# 遞迴可以讓我們從根節點開始，逐層地訪問每個節點   

