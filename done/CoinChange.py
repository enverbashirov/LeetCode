from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, coins, amount):
        self.coins = coins
        self.amount = amount
        print("init")

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] =0

        coins.sort()
        
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+ dp[a-c])
                else:
                    break

        return  dp[amount] if dp[amount] != amount+1 else -1
    
    def main(self):
        print(self.coinChange(self.coins, self.amount))
        return

if __name__ == "__main__":
    coins = [1,2,5]; amount = 11 #Output: 3
    # coins = [2]; amount = 3 #Output: -1
    # coins = [1]; amount = 0 #Output: 0

    sol = Solution(coins, amount)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
