# 尋找在給定時間段（陣列）內，買入和賣出之間的最大差價 

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')      #初始化極端大的數字，才能確保第10行順利執行
        max_profit = 0        #初始化利潤
        for current_price in prices:
            if current_price < min_price:
                min_price = current_price
            else:
                max_profit = max(max_profit, current_price - min_price)  #更新最大利潤
        return max_profit         

    
##題目重點
# coder常常用 float('inf') 或 float('-inf') 來初始化「極端大或極端小的數字」



