from timeit import default_timer as timer
from typing import List
# import re

class Solution:
    def __init__(self, s):
        self.s = s
        print("init")

    def isPalindrome(self, s: str) -> bool:
        # REGEX
        # s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # NON-REGEX
        s = [c.lower() for c in s if c.isalnum()]
        return s[:int(len(s)/2)] == s[int(len(s)/2) + len(s)%2:][::-1]

    def main(self):
        print(self.isPalindrome(s))
        return

if __name__ == "__main__":
    # s = "A man, a plan, a canal: Panama" # True
    s = "race a car" # False
    # s = "potatop" # True
    # s = " " # True

    sol = Solution(s)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
