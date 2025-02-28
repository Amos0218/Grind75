import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            # 計算距離
            distance = x**2 + y**2
            #heapq 是根據元組的 第一個元素（即 item[0]）來進行排序的
            heapq.heappush(heap, (distance, [x, y]))   # 使用堆儲存 (距離, 該點座標) 元組
        
        # 把堆中最接近原點的 K 個點取出
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])  # 取出點的座標
        
        return result

##題目重點
# 1.heapq.heappush(heap, item)：這是 Python 標準庫中 heapq 模組的一個函數，
#  用來將資料 item 加入到堆 heap 中，並自動保持堆的排序特性（最小堆）。
#  也就是說，每次插入資料後，堆中最小的元素會排在最前面   

# 2.heapq.heappop(heap)：這是 heapq 模組中的另一個函數，它會從堆中取出最小的元素並移除它。
# 因為堆是最小堆，所以這會取出距離原點最近的元素