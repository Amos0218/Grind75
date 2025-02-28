# 給定一個 nums 陣列，找出所有 不重複 的 三個數 使其總和為 0

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 先排序
        res = []

        # 步驟一，開始遍歷 nums，固定 nums[i]
        for i in range(len(nums) - 2):  # 固定 nums[i]
            if i > 0 and nums[i] == nums[i - 1]:  # 說明 nums[i] 的組合已經計算過
                continue       # 跳過重複數字
            
            # 步驟二，雙指針尋找 left 和 right
            left, right = i + 1, len(nums) - 1  
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1  # 總和太小，left 右移
                elif total > 0:
                    right -= 1  # 總和太大，right 左移
                else:
                    res.append([nums[i], nums[left], nums[right]])  # 找到解

                    # 步驟三，跳過重複數字
                    while left < right and nums[left] == nums[left + 1]:  
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res
    

##題目重點
# 1.雙指針方法：
#   在固定 nums[i] 之後，使用兩個指針，left 和 right，
#   來分別指向 i 之後和 nums 的末尾，並根據總和的結果來移動指針

# 2.三元組需要三個數字，所以 i 必須至少指向倒數第三個數字

# 3.步驟一用來跳過 nums[i] 的重複值
#   步驟三用來跳過雙指針 left, right 所產生的重複組合