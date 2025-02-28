from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = [root] # 初始化一個隊列，將根節點放入隊列

        while queue:
            # 計算當前層的節點數量
            level_size = len(queue)

            # 準備一個空列表來存放當前層的節點值
            level_values = []

            # 遍歷當前層的所有節點
            for _ in range(level_size):
                node = queue.pop(0)  # 取出隊列的首節點

                # 將該節點的值加入當前層的列表
                level_values.append(node.val)

                # 如果有左子節點，將它加入隊列，為下一層做準備
                if node.left:
                    queue.append(node.left)

                # 如果有右子節點，將它加入隊列，為下一層做準備
                if node.right:
                    queue.append(node.right)

            # 將當前層的結果加入到最終的結果列表中
            result.append(level_values)

        return result
    
##題目重點
# 1. 隊列的先進先出（FIFO）特性使得我們可以確保先處理父節點，
# 再處理它的子節點。這樣能夠保證我們是逐層遍歷    
# 2. 使用queue.pop(0) 來取出並移除隊列的第一個元素