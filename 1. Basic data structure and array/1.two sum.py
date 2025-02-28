# 題目要求你從一個整數數組中找出兩個數字，
#  使得它們的和等於一個目標值（target）。
#  你需要返回這兩個數字的索引，並且這兩個數字的順序不重要


##暴力解法

from typing import List       # 引入List（因為下面的程式碼有用到型別註解）
 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # j 從 i+1 開始，避免重複
                if nums[i] + nums[j] == target:
                    return [i, j]  # 直接回傳結果，找到後立即結束
        return []  # 理論上不會發生，因為題目保證有唯一解
    


##哈希表解法（運用鍵值對）

from typing import List      # 引入List（因為下面的程式碼有用到型別註解）

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}                    # 哈希表，用來存儲數字與其對應的索引index
        for i, num in enumerate(nums):  # 用enumerate遍歷每個數字(預設回傳包含索引與值的元組)
            complement = target - num   # 計算 complement(也就是我們要找的另一個數)
            if complement in num_map:   # 檢查 complement 是否已經出現過
                return [num_map[complement], i]         # 若找到 complement，回傳其索引
            num_map[num] = i    # 如果沒有，將當前數字及其索引存入哈希表
        return []               # 理論上不會發生，因為題目保證有解    
    
##題目重點
# 1. self 是每個類別方法中的第一個參數，它代表當前函式所屬的物件實例，
#    並讓你在函式內存取該物件的屬性和呼叫其他方法
#2. return [] 用來表示 “目前沒有結果” 或 “沒有需要處理的資料”


