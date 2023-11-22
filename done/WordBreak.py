from timeit import default_timer as timer
from typing import List
    
class Solution:
    def __init__(self, s, wordDict):
        self.s = s
        self.wordDict = wordDict
        print("init")

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        max_len = max(map(len, wordDict))  # The maximum length of a word in the dictionary

        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1): # Only consider words that could fit
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]
            

    def main(self):
        print(self.wordBreak(self.s, self.wordDict))
        return

if __name__ == "__main__":
    # s = "leetcode"; wordDict = ["leet","code"] # Output: true
    # s = "applepenapple"; wordDict = ["apple","pen"] # Output: true
    s = "catsandog"; wordDict = ["cats","dog","sand","and","cat"] #Output: false
    
    sol = Solution(s, wordDict)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")