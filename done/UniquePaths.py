from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, m, n):
        self.m = m
        self.n = n
    
    
    def uniquePaths(self, m: int, n: int) -> int:
        # if m == 1 and n == 1: return 1
        if m == 1 or n == 1: return 1

        def factorial(f):
            ans = f
            for i in range(1, f):
                ans *= i
            return ans
        
        a = m+n-2
        b = min(m-1, n-1)

        return int(factorial(a) / (factorial(b) * factorial(a-b)))
    
    def main(self):
        start = timer()
        print(self.uniquePaths(self.m, self.n))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # m = 3; n = 7 # Output: 28
    # m = 3; n = 2 # Output: 3
    # m = 1; n = 1 # Output: 1
    # m = 1; n = 2 # Output: 1
    # m = 2; n = 2 # Output: 2
    # m = 3; n = 3 # Output: 6
    m = 1; n = 10 # Output: 1

    sol = Solution(m, n)
    sol.main()