from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, s, t):
        self.s = s
        self.t = t
        print("init")

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def main(self):
        print(self.isAnagram(self.s, self.t))
        return

if __name__ == "__main__":
    # s = "anagram"; t = "nagaram"
    s = "rat"; t = "car"

    sol = Solution(s, t)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
