# 回傳「無重複字符的最長子串」的長度

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0  # 用來記錄最長不重複子字串的長度
        left = 0  # 左指針
        seen = set()  # 用來存放當前視窗內的字母，避免重複
        
        for right in range(len(s)):   # 右指針向右移動
            while s[right] in seen:   # 有重複的字母的話
                seen.remove(s[left])  # 移除左邊界的字母
                left += 1   #移動左指針縮小視窗
            
            seen.add(s[right])  # 把當前字母加入 set
            max_length = max(max_length, right - left + 1)  # 更新最大長度（右邊界減左邊界加一）
        
        return max_length
    
##題目重點
# 1. 運用滑動窗口（Sliding Window，動態調整範圍 來找出最長的不重複子字串
# 2. 熟悉不同序列的操作（整理在備忘錄）