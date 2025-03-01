# 深度拷貝（Clone）無向圖，並使用 DFS（深度優先搜尋） 來實現

from typing import Optional

# 定義圖的節點結構
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val  # 節點的值
        self.neighbors = neighbors if neighbors is not None else []  # 鄰居節點的列表

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None  

        oldToNew = {}  # 建立字典來記錄「舊節點 -> 新節點」的對應關係

        def dfs(node):
            #1️⃣
            if node in oldToNew:  
                return oldToNew[node]  # 如果該節點已複製，直接返回對應的新節點
            
            #2️⃣
            copy = Node(node.val)  # 創建當前節點的副本
            oldToNew[node] = copy  # 記錄舊節點與新節點的對應關係
            
            for neighbor in node.neighbors:  # 遍歷當前節點的所有鄰居
                copy.neighbors.append(dfs(neighbor))  # 遞歸複製所有鄰居
            
            return copy  # 返回複製的節點
        
        return dfs(node)  # 從輸入的 `node` 開始複製整個圖  
    
    
## 題目重點
# 1️⃣ 在「if node in oldToNew」的地方，`oldToNew` 字典的作用是確保 **每個節點只會被複製一次**，
#    這樣能夠避免無窮遞迴（例如當圖是循環結構時），也能提高效率，避免重複創建相同節點。
#
# 2️⃣ 在「copy = Node(node.val)」的地方，如果沒有用 `Node()` 包起來，那 `copy` 就只是一個數值，
#    而不是一個真正的「節點」，這樣我們就 **無法存儲 `neighbors`**，導致複製圖失敗！ 