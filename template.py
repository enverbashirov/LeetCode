from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self):
        print("init")

    def main(self):
        start = timer()
        # Function call
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    sol = Solution()
    sol.main()