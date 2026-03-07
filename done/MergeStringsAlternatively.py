from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        print("init")

    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = []
        s1, s2 = len(word1), len(word2)
        i = 0
        while(i < min(s1, s2)):
            r.append(word1[i])
            r.append(word2[i])
            i += 1
        
        if i < s1:
            r.append(word1[i:])
        if i < s2:
            r.append(word2[i:])

        return str().join(r)
    
    def main(self):
        start = timer()
        # Function call
        print(self.mergeAlternately(self.word1, self.word2))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # word1 = ""; word2 = "" # Output: ""
    # word1 = "abc"; word2 = "" # Output: "abc"
    # word1 = ""; word2 = "abc" # Output: "abc"
    # word1 = "a"; word2 = "abc" # Output: "aabc"
    # word1 = "abc"; word2 = "pqr" # Output: "apbqcr"
    # word1 = "ab"; word2 = "pqrs" # Output: "apbqrs"
    word1 = "abcd"; word2 = "pq" # Output: "apbqcd"
 
    sol = Solution(word1, word2)
    sol.main()