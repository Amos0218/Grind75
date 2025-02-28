# 給定一個已排序的數組 nums 和一個目標值 target，使用二分搜尋法來查找
#  target 在數組中的索引。如果 target 存在，返回其索引，否則返回 -1

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 設定左右邊界

        while left <= right:
            mid = (left + right) // 2  # 計算中間索引
            if nums[mid] == target:
                return mid  # 找到目標值，回傳索引
            elif nums[mid] < target:
                left = mid + 1  # 往右半部搜尋
            else:
                right = mid - 1  # 往左半部搜尋
        
        return -1  # 沒找到則回傳 -1
    
##題目重點    
#學會正確使用二分搜尋法，
# O(log n) 複雜度：二分搜尋法每次將搜尋範圍減半