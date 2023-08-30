from timeit import default_timer as timer
from typing import List


class Solution:
    def __init__(self, n, bad):
        self.n = n
        self.bad = bad
        print("init")

    # The isBadVersion API is already defined for you.
    def isBadVersion(self, version: int) -> bool:
        return True if version >= self.bad else False
        
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return 1
        i, j = 1, n
        while j != int((i + j) / 2) and i != int((i + j) / 2):
            # print(i, int((i + j) / 2), j)
            if (self.isBadVersion(int((i + j) / 2))): j = int((i + j) / 2)
            else: i = int((i + j) / 2)
        # print(i, int((i + j) / 2), j)

        if self.isBadVersion(i): return i
        if self.isBadVersion(j): return j

    
    def main(self):
        print(self.firstBadVersion(self.n))
        return

if __name__ == "__main__":
    n = 50; bad = 50
    # n = 1; bad = 1

    sol = Solution(n, bad)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
