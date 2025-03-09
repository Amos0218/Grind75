#給定一個整數數組 nums，要求你計算一個新數組 output，
# 其中 output[i] 是nums中除了 nums[i] 本身以外所有元素的乘積。

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n  # 初始化結果陣列，每個元素設為 1

        ##⭐️
        left_product = 1
        for i in range(n):
            output[i] = left_product 
            left_product *= nums[i]  # 更新左邊乘積

        right_product = 1
        for i in range(n - 1, -1, -1):  # 從右邊開始遍歷
            output[i] *= right_product  # 更新結果，將右邊乘積相乘
            right_product *= nums[i]  # 更新右邊乘積

        return output
    

##題目重點    
# 假設 nums = [1, 2, 3, 4]，遍歷過程是這樣的：
##左    
# 	•	初始化：left_product = 1
# 	•	第一次遍歷：output[0] = 1，更新 left_product = 1 * 1 = 1
# 	•	第二次遍歷：output[1] = 1，更新 left_product = 1 * 2 = 2
# 	•	第三次遍歷：output[2] = 2，更新 left_product = 2 * 3 = 6
# 	•	第四次遍歷：output[3] = 6，更新 left_product = 6 * 4 = 24
#   此時 output 的結果為 [1, 1, 2, 6]，它儲存的是每個位置左邊的乘積。
##右
# 	•	初始化：right_product = 1
# 	•	第一次遍歷：output[3] = 6 * 1 = 6，更新 right_product = 1 * 4 = 4
# 	•	第二次遍歷：output[2] = 2 * 4 = 8，更新 right_product = 4 * 3 = 12
# 	•	第三次遍歷：output[1] = 1 * 12 = 12，更新 right_product = 12 * 2 = 24
# 	•	第四次遍歷：output[0] = 1 * 24 = 24，更新 right_product = 24 * 1 = 24

#   此時 output 的結果為 [24, 12, 8, 6]，它儲存的是每個位置左邊和右邊的乘積。



        