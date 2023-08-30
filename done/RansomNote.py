from timeit import default_timer as timer
from typing import List


class Solution:
    def __init__(self, ransomNote, magazine):
        self.ransomNote = ransomNote
        self.magazine = magazine
        print("init")

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        while ransomNote != '':
            print(ransomNote, magazine)
            c = ransomNote[0]
            if ransomNote.count(c) > magazine.count(c):
                return False
            ransomNote = ransomNote.replace(c, '')
            magazine = magazine.replace(c, '')

        return True
    
    def main(self):
        print(self.canConstruct(self.ransomNote, self.magazine))
        return

if __name__ == "__main__":
    # ransomNote = "a"; magazine = "b" # False
    ransomNote = "a"; magazine = "a" # False
    # ransomNote = "aa"; magazine = "ab" # False
    # ransomNote = "aa"; magazine = "aab" # True

    sol = Solution(ransomNote, magazine)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
