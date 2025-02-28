# Kadane’s Algorithm

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  # 初始化最大和
        current_sum = 0  # 當前子陣列的和
        
        for n in nums:
            # 這裡選擇加上當前數字還是重新開始新的子陣列
            current_sum = max(current_sum + n, n)
            # 更新最大和
            max_sum = max(current_sum, max_sum)
        
        return max_sum

##題目重點
# 遍歷陣列時，我們要動態地計算每個元素所在的當前子陣列的和，
# 動態規劃的好處之一就是它不需要對數列進行排序
