from timeit import default_timer as timer
from typing import List
import string
import re

class Solution:
    def __init__(self, s, words):
        self.s = s
        self.words = words
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        i = 0
        ans = []

        while(i+(len(words[0])*len(words)) <= len(s)):
            sub = [s[i:i+len(words[0])] for i in range(i, i+(len(words[0])*len(words)), len(words[0]))]
            for w in words:
                # print('!', i, s, words, sub, ans)
                if w in sub: sub.remove(w)
                else: break

            # print(i, s, words, sub, ans)

            if len(sub) == 0:
                ans.append(i)
            i += 1
        # print(i, s, words, sub, ans)
        return ans

    def main(self):
        start = timer()
        print(self.findSubstring(self.s, self.words))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # s = "barfoothefoobarman"; words = ["foo","bar"] # Output: [0,9]
    # s = "wordgoodgoodgoodbestword"; words = ["word","good","best","word"] # Output: []
    # s = "barfoofoobarthefoobarman"; words = ["bar","foo","the"] # Output: [6,9,12]
    s = "wordgoodgoodgoodbestword"; words = ["word","good","best","good"] # Output: [8]
    # s = "wordgoodgoodgoodbestword"; words = ["word","good","best","word"] # Output: []
    # s = "ababaab"; words = ["ab","ba","ba"] # Output: [1]
    # s = "ababaab"; words = ["ab","ba","aa"] # Output: []

    sol = Solution(s, words)
    sol.main()