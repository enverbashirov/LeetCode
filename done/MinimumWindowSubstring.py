from timeit import default_timer as timer
from typing import List
from collections import Counter

class Solution:
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = Counter()
        minLength = len(s) + 1
        res = ""

        l = 0
        for r in range(len(s)):
            have[s[r]] += 1

            while all(have[c] >= need[c] for c in need):
                minLength = min(minLength, r - l + 1)
                if minLength == r - l + 1:
                    res = s[l:r + 1]
                have[s[l]] -= 1
                l += 1

        return res if minLength <= len(s) else ""
    
    def main(self):
        start = timer()
        print(self.minWindow(self.s, self.t))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    s = "ADOBECODEBANC"; t = "ABC" # Output: "BANC"
    # s = "a"; t = "a" # Output: "a"
    # s = "a"; t = "aa" # Output: ""
    # s = "ABC"; t = "ACB"
    # s = "bdab"; t = "ab" # "ab"

    sol = Solution(s, t)
    sol.main()