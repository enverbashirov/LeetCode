from typing import List
from timeit import default_timer as timer
# import numpy as np

class Solution:
    def __init__(self):
        print("init")

    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if m*k > len(arr):
            return False

        for i in range(0, len(arr)-(m*k-1)):
            tarr = arr[i:i+m] * k
            if tarr == arr[i:i+(m*k)]:
                return True

        return False

    def main(self):
        arr = [2,2,2,2,2]; m = 2; k = 3
        print(self.containsPattern(arr, m, k))

if __name__ == "__main__":
    sol = Solution()
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
