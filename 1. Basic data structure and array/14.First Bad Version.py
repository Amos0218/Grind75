# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(version: int) -> bool:
    bad_version = 4  # 假設壞版本是第 4 個
    return version >= bad_version  # 當 version >= 4，視為壞版本

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # 正確的初始化
        
        while left < right:  # 確保 left 會停在第一個壞版本
            mid = (left + right) // 2  # 避免整數溢位
            
            if isBadVersion(mid):  
                right = mid  # mid 可能是第一個壞版本，所以 right = mid
            else:
                left = mid + 1  # mid 是好版本，所以 left = mid + 1
            
        return left  # left 會停在第一個壞版本
    
##題目重點
# 運用二分搜尋法，找出第一個壞版本    