from typing import Optional

# 定義圖的節點結構
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val  # 節點的值
        self.neighbors = neighbors if neighbors is not None else []  # 鄰居節點的列表

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None  # 如果圖是空的，直接返回 None

        oldToNew = {}  # 建立字典來記錄「舊節點 -> 新節點」的對應關係

        def dfs(node):
            if node in oldToNew:  
                return oldToNew[node]  # 如果該節點已複製，直接返回對應的新節點
            
            copy = Node(node.val)  # 創建當前節點的副本
            oldToNew[node] = copy  # 記錄舊節點與新節點的對應關係
            
            for neighbor in node.neighbors:  # 遍歷當前節點的所有鄰居
                copy.neighbors.append(dfs(neighbor))  # 遞歸複製所有鄰居
            
            return copy  # 返回複製的節點
        
        return dfs(node)  # 從輸入的 `node` 開始複製整個圖  