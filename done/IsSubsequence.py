from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, s: str, t: str):
        self.s = s
        self.t = t
        print("init")

    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while(i < len(s) and j < len(t)):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s): 
            return True
        
        return False

    def main(self):
        start = timer()
        print(self.isSubsequence(self.s, self.t))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # s, t = "abc", "ahbgdc" # Output: true
    # s, t = "axc", "ahbgdc" # Output: false
    s, t = "acb", "ahbgdc" # Output: false

    sol = Solution(s, t)
    sol.main()