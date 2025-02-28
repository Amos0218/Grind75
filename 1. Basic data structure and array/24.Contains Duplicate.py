#給定一個整數數組 nums，判斷是否有任何一個元素出現至少兩次。
#如果有，返回 True，否則返回 False

#寫法一
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for n in nums:
            if n in a:
                return True
            a.add(n)     #set用add(), list 用append()
        return False        
    
#寫法二
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #集合（set）會自動去除重複的元素，所以如果 nums 中有重複的元素，
        # 轉換為集合後的長度會比原來的長度小
        return len(nums) != len(set(nums))    

##題目重點
# a = {}      創建空字典
# a = set()   創建空集合