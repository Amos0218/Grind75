#計算一個二維網格（grid）中由 1（陸地）組成的島嶼數量，
# 其中島嶼由水平或垂直相鄰的 1 組成，0（水）則是分隔島嶼的部分

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        #1️⃣計算列數、行數
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            """ 深度優先搜尋，將島嶼標記為已訪問 """
            #2️⃣
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return  # 超出邊界或遇到水域（已訪問）

            grid[r][c] = '0'  # 標記已訪問

            # 遞迴搜尋四個方向
            dfs(r + 1, c)  # 下
            dfs(r - 1, c)  # 上
            dfs(r, c + 1)  # 右
            dfs(r, c - 1)  # 左
        
        island_count = 0  # 計算島嶼數量

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # 遇到新的島嶼
                    island_count += 1  # 增加島嶼數量
                    dfs(r, c)  # 進行 DFS 搜索，標記整個島嶼

        return island_count
    
    ##題目重點
    #1️⃣len(grid[0])：計算第一列的元素個數（就是行數）
    #2️⃣：這個 return 的目的是 停止進一步的遞迴，而不是返回任何結果
    
