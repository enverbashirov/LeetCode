from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, s):
        self.s = s
        print("init")

    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, i, j = 0, 0, 0
        for c in s:
            while (c in s[i:j]): i += 1 
            if ans < (j-i)+1: ans += 1 
            j += 1
            # print(ans, s[i:j])

        return ans

    def main(self):
        print(self.lengthOfLongestSubstring(self.s))
        return

if __name__ == "__main__":
    s = "" #Output: 0
    # s = "abcabcbb" #Output: 3
    # s = "bbbbb" #Output: 1
    # s = "pwwkew" #Output: 3
    # s = "abbbc" #Output: 2
    # s = "nfasdkj12098 64!" #Output: 16
    # s = "abcadabcea" #Output: 5

    sol = Solution(s)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
