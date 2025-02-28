#給定兩個字符串 s 和 t，判斷 t 是否是 s 的字母重排，即是否是 s 的 anagram

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 如果兩個字串長度不相等，直接返回False
        if len(s) != len(t):
            return False
        # 計算字母頻率並比較
        return Counter(s) == Counter(t)      

##題目重點
#Counter用來計算可迭代對象中每個元素的出現次數（頻率）。
#它會返回一個字典類型的對象，其中鍵是元素，值是該元素的出現次數