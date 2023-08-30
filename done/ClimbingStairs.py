from timeit import default_timer as timer
from typing import List


class Solution:
    def __init__(self, n):
        self.n = n
        # self.count = 0
        print("init")

    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
    
    # Time limit exceeded
    # def climbStairs(self, n: int) -> int:
    #     if n == 0 or n == 1: return 1
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # Time limit exceeded
    # def climbStairs(self, n: int) -> int:
    #     if n == 0: self.count += 1
    #     if n - 1 >= 0: self.climbStairs(n - 1)
    #     if n - 2 >= 0: self.climbStairs(n - 2)

    #     return self.count
    
    def main(self):
        print(self.climbStairs(self.n))
        return

if __name__ == "__main__":
    # n = 2 # 2
    # n = 3 # 3
    n = 45

    sol = Solution(n)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
