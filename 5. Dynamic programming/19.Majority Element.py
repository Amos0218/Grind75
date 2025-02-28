# 找出出現次數最多的元素

##摩爾投票法(空間效率高)

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None  # 用來儲存候選眾數
        count = 0  # 記錄候選數字的計數
        
        for num in nums:
            if count == 0:
                candidate = num  # 如果計數為 0，更新候選者
            count += (1 if candidate == num else -1)  # 如果是候選者，計數加1，否則減1
        
        return candidate  # 返回最終的候選者（眾數）   


##使用Counter計算出現頻率，然後比較

from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_count = Counter(nums)  # 計算每個數字的出現次數

        max_count = 0  # 記錄當前最大出現次數
        answer = None  # 儲存最終的眾數

        for char, count in nums_count.items():  # 遍歷每個數字及其出現次數
            if count > max_count:  # 如果該數字的出現次數比目前的 max_count 還多
                max_count = count  # 更新最大出現次數
                answer = char  # 更新答案為該數字
        
        return answer  # 返回出現次數最多的數字

 