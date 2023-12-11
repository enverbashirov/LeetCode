from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, s):
        self.s = s

    def myAtoi(self, s: str) -> int:
        min, max = -1 * (2 ** 31), (2 ** 31) - 1 # [-2^31, 2^31] 32-bit
        ans = ''
        s = s.lstrip()
        
        if s == '': return 0
        if s[0] == '-': ans = '-'; s = s[1:]
        elif s[0] == '+': s = s[1:]

        for c in s:
            try: 
                int(c)
            except ValueError:
                print('ValueError')
                break
            ans = ans + c

        try: 
            ans = int(ans) 
        except ValueError: 
            return 0

        if ans < -1 * (2 ** 31): ans = -1 * (2 ** 31)
        if ans > (2 ** 31) - 1: ans = (2 ** 31) - 1
        return ans

    def main(self):
        print(self.myAtoi(self.s))

if __name__ == "__main__":
    # s = "42" # Output: 42
    # s = "   -42   " # Output: -42
    # s = "4193 with words" # Output: 4193
    s = "   -004193 bakak 1981 " # Output: -4193

    sol = Solution(s)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")