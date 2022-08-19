from timeit import default_timer as timer
from typing import List
import numpy as np

class Solution:
    def __init__(self, s, shifts):
        self.s = s
        self.shifts = shifts
        print("init")

    # First approach
    # def shift(self, letter: str, shift: int):
    #     letters = 'abcdefghijklmnopqrstuvwxyz'
    #     return letters[(letters.index(letter) + shift) % len(letters)]

    # def shiftingLetters(self, s: str, shifts: List[int]) -> str:
    #     for i, shift in enumerate(shifts):
    #         for j in range(0, i+1):
    #             s = s[:j] + self.shift(s[j], shift) + s[j+1:]
    #     return s
    
    # Second approach   
    # def shiftingLetters(self, s: str, shifts: List[int]) -> str:
    #     s = list(s)
    #     for i in range(len(shifts)-1, 0, -1):
    #         s[i] = chr((((ord(s[i]) + shifts[i]) - 97 ) % 26 ) + 97)
    #         shifts[i-1] += shifts[i] % 26
    #     s[0] = chr((((ord(s[0]) + shifts[0]) - 97 ) % 26 ) + 97)
    #     s = ''.join(s)
    #     return s

    # Third approach
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        tot = 0
        for i in range(len(shifts)-1, -1, -1):
            tot = (tot + shifts[i]) % 26
            s[i] = chr((((ord(s[i]) + tot) - 97 ) % 26 ) + 97)
        s = ''.join(s)
        return s

    def main(self):
        print(self.shiftingLetters(self.s, self.shifts))
        return

if __name__ == "__main__":
    s = "abc"; shifts = [3,5,9] #rpl
    # s = "aaa"; shifts = [27,28,29] #rpl
    # s = "z"; shifts = [3] #c
    #s = "aaa"; shifts = [1,2,3] #gfd

    sol = Solution(s, shifts)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
