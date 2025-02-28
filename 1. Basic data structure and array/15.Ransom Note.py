#給定兩個字串 ransomNote 和 magazine，
#請判斷能否從 magazine 中取出足夠的字母來組成 ransomNote

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for char, count in ransom_counter.items(): 
            #檢查 magazine 中的字母char是否能滿足 ransomNote 所需的數量count
            if magazine_counter[char] < count:
                return False

        return True    

solution = Solution()

#題目重點
#確認數量是否足夠
#Counter 是 用來計數 的字典類型
#Counter['key'] 取值時，不存在的鍵會回傳 0
#可用 +、-、.elements()、.most_common() 進行操作
