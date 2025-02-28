#給定樓梯的總階數 n，每次可以爬 1 或 2 階，要求計算有多少種不同的走法可以爬到頂端

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev1 = 1  # f(1)
        prev2 = 2  # f(2)
        
        for i in range(3, n+1):
            curr = prev1 + prev2  # 計算 f(n) = f(1) + f(2)
            prev1 = prev2  # f(n-2) 滾動到下一步
            prev2 = curr   # f(n-1) 滾動到下一步
        
        return prev2  # 最後的 prev2 就是 f(n)

        
##題目重點
#1.這是一題動態規劃DP的問題，要用費氏數列的概念解題
#2.運用滾動變數的技巧，只需要用到前兩個值