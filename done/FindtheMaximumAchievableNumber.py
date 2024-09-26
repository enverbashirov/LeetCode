from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, num, t):
        self.num = num
        self.t = t

    def theMaximumAchievableX(self, num: int, t: int) ->int:
        return num + (t * 2)

    def main(self):
        start = timer()
        print(self.theMaximumAchievableX(self.num, self.t))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    num = 4; t = 1 # Output: 6
    # num = 3; t = 2 # Output: 7

    sol = Solution(num, t)
    sol.main()