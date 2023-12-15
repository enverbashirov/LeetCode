from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, s):
        self.s = s

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str
    
    def main(self):
        start = timer()
        print(self.longestPalindrome(self.s))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # s = "babad" # Output: "bab"
    s = "baabd" # Output: "bab"
    # s = "cbbd" # Output: "bb"

    sol = Solution(s)
    sol.main()