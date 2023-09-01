from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("init")

    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]
    
    def main(self):
        print(self.addBinary(self.a, self.b))
        return

if __name__ == "__main__":
    # a = "11"; b = "1" # 100
    a = "1010"; b = "1011" # 10101

    sol = Solution(a, b)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
