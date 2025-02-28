# 在給定的區間列表 intervals 中插入一個新的區間 newInterval，並確保結果仍然是「不重疊的排序區間」

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]  # ✅ 確保返回的是 List[List[int]]
        
        result = []
        i = 0    #遍歷 intervals 的索引
        n = len(intervals)

        # 1️⃣ **先加入不重疊且在 newInterval 之前的區間**
        while i < n and intervals[i][1] < newInterval[0]:      #intervals[i] 的結束點小於 newInterval 的開始點
            result.append(intervals[i])
            i += 1

        # 2️⃣ **合併重疊區間**
        while i < n and intervals[i][0] <= newInterval[1]:  # 只要有重疊就更新 newInterval
            newInterval[0] = min(newInterval[0], intervals[i][0])  #更新 newInterval 的 開始點
            newInterval[1] = max(newInterval[1], intervals[i][1])  #更新 newInterval 的 結束點
            i += 1
        result.append(newInterval)  # 插入合併後的區間

        # 3️⃣ **加入 newInterval 之後的區間**
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
    
##題目重點
# 這題的核心在於遍歷 intervals 時需要分三種情況：
# 1.	完全不重疊且在左側：直接加入 result
# 2.	有重疊：更新 newInterval，合併區間
# 3.	完全不重疊且在右側：直接加入 result    