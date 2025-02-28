#給定一個 m x n 的二維矩陣 image 和一個起始像素 sr, sc，以及一個顏色 Color
#從起始位置 (sr, sc) 開始，將相同顏色的相鄰像素塗上 newColor。
#需要確保這個填充操作是連通的，即相鄰的像素會繼續被填充

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        
        # 如果原始顏色和目標顏色相同，則無需更改
        if original_color == color:
            return image

        def dfs(r, c):        #定義 列索引 跟 行索引（橫列直行）

            # 檢查邊界
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original_color:
                return     #結束當前的遞迴呼叫
            # 改變當前像素顏色
            image[r][c] = color
            
            # 遞歸處理四個方向的相鄰像素
            dfs(r + 1, c)  # 下
            dfs(r - 1, c)  # 上
            dfs(r, c + 1)  # 右
            dfs(r, c - 1)  # 左
        
        # 從起始像素開始執行 DFS
        dfs(sr, sc)
        
        return image

##題目重點
#檢查越界
# 1.r < 0 or r >= len(image)檢查列是否越界，r < 0 或 r >= 圖片的列數
# 2.c < 0 or c >= len(image[0])檢查行是否越界，c < 0 或 c >= 圖片的行數
# 3.image[r][c] != original_color檢查當前像素顏色是否與起始顏色一致，不一致則停止繼續處理，因為這代表已經被改過了
# 4. return 在遞迴中可以用來終止當前遞迴        