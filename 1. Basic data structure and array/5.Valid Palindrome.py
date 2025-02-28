# 給定一個字符串 s，判斷它是否是回文串

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 過濾非字母數字並轉小寫
        filtered_s = "".join(char.lower() for char in s if char.isalnum())

        # 定義雙指針
        left, right = 0, len(filtered_s) - 1
        #直到左邊指針碰到右邊指針之前
        while left < right:
            if filtered_s[left] != filtered_s[right]:  # 不相等則不是回文
                return False
            left += 1
            right -= 1
        
        return True  # 檢查完畢，為回文
    

##題目重點
# 1.  .join()回傳的是字串
# 2.  用.islanum()檢查 char 是否是字母或數字，只有是字母或數字的字符才會被保留
# 3.運用雙指針left,right遍歷所有元素    