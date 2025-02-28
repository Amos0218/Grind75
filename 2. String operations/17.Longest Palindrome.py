#題目要求我們找到一個給定字串中的 最長回文子串。

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        str_counter = Counter(s)
        max_length = 0
        odd_found = False  # 是否有奇數次的字母
        
        for char, count in str_counter.items():  # 正確的寫法
            if count % 2 == 0:  
                max_length += count  # 偶數個字母可全部使用
            else:
                max_length += count - 1  # 奇數次的字母，扣掉 1 個變偶數
                odd_found = True  # 代表至少有一個奇數字母
        
        if odd_found:
            max_length += 1  # 可以放 1 個奇數次字母在回文的中央
        
        return max_length