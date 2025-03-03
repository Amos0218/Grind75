from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1️⃣ 初始化 DP 陣列，大小為 amount + 1，設為無窮大(表示尚未計算過)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 湊出金額 0 的話不需要任何硬幣
        
        # 遍歷每個金額
        for i in range(1, amount + 1):
            # 2️⃣
            for coin in coins:
                if i - coin >= 0:  
                    dp[i] = min(dp[i], dp[i - coin] + 1)   # 3️⃣ 更新dp[i]的值
        

        # 如果無法湊出該金額，返回 -1
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
        
##題目重點
# 在 1️⃣ 中，dp[i] 代表湊出金額 i 所需的最少硬幣數量

# 在 2️⃣ 中，如果 i - coin >= 0，這意味著金額 i 能夠由
# 金額 i - coin 加上這個硬幣（coin) 組成。換句話說，這個硬幣能幫我們湊出金額 i

# 在 3️⃣ 中，dp[i - coin] 是湊出金額 i - coin 所需的最少硬幣數，而加上 1 是因為我們又使用了一個coin
        
