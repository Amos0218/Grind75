# 給定一個二叉樹的根節點，請你判斷該樹是否為平衡二叉樹
# 如果一棵二叉樹的每個節點的左右子樹高度差不大於 1，則這棵二叉樹是平衡的

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node): 
            if not node:
                return 0  # 空節點的高度為 0
            
            left_height = check_height(node.left)
            if left_height == -1:       #收到第27行的判斷結果後
                return -1  # 左子樹已經不平衡，直接返回
            
            right_height = check_height(node.right)
            if right_height == -1:      #收到第27行的判斷結果後
                return -1  # 右子樹已經不平衡，直接返回
            
            if abs(left_height - right_height) > 1:
                return -1  # 當前節點不平衡，返回 -1  
            
            return max(left_height, right_height) + 1  # 回傳該節點的高度，不需要另外設變數紀錄
        
        return check_height(root) != -1  # 判斷整棵樹是否平衡

##題目重點    
# 1.運用遞迴計算其左子樹和右子樹的高度，然後檢查其左右子樹是否平衡
# 2.本題使用後序遍歷，三種遍歷的特色如下：
#   前序遍歷的順序是：先處理當前節點本身，再處理左子樹，再處理右子樹。
#   中序遍歷的順序是：先處理左子樹，再處理當前節點本身，再處理右子樹。
#   後序遍歷的順序是：先處理左子樹，再處理右子樹，再處理當前節點本身
    
