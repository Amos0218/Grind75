# 給你兩個二進制字串 a 和 b，請你回傳它們的二進制和（以二進制表示）

#寫法一
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []  # 用來存放計算結果
        carry = 0  # 進位變數
        i, j = len(a) - 1, len(b) - 1  # 從最後一位開始遍歷

        while i >= 0 or j >= 0 or carry:  # 只要 a 或 b 還沒遍歷完，或有進位
            digit_a = int(a[i]) if i >= 0 else 0  # 若 i 超出範圍則視為 0
            digit_b = int(b[j]) if j >= 0 else 0  # 若 j 超出範圍則視為 0
            
            total = digit_a + digit_b + carry  # 計算這一位的總和
            carry = total // 2  # 進位（當 total >= 2 時，進位變為 1）
            result.append(str(total % 2))  # 只保留個位數（0 或 1）

            i -= 1  # 移動到前一位
            j -= 1

        return ''.join(result[::-1])  # 反轉結果並轉成字串輸出

#寫法二
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 將二進制字串轉換為十進制整數，進行加法，再轉回二進制字串
        return bin(int(a, 2) + int(b, 2))[2:]

##題目重點
# 1.用list[::-1] 代表從後往前遍歷，可達到反轉的效果
# 2. bin(...)將加法結果轉換回二進制字串，
# 但是Python會自動在結果的最前面加上一個前綴 '0b' ,標示這個數字是二進制格式
# 所以要用[2:]，從索引 2 開始取剩下的部分


