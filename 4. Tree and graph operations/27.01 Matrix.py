from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # 1. 初始化 dist 矩陣，並設置 queue 用來進行 BFS
        m, n = len(mat), len(mat[0])  # m 是行數，n 是列數
        dist = [[float('inf')] * n for _ in range(m)]  # 初始化 dist 矩陣為 inf
        queue = deque()  # 使用 deque 來存儲 BFS 過程中的節點

        # 2. 將所有的 0 的位置放入 queue，並更新 dist 中 0 的距離為 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))  # 將 0 的座標加入 queue

        # 3. 執行 BFS
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上、下、左、右四個方向
        while queue:
            x, y = queue.popleft()  # 取出隊列中的座標
            # 訪問相鄰的格子
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 確保新座標在矩陣範圍內
                if 0 <= nx < m and 0 <= ny < n:
                    # 更新距離並將該位置加入隊列
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))

        # 4. 返回最終的 dist 矩陣
        return dist