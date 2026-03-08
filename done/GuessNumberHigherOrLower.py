import random
from timeit import default_timer as timer

class Solution:
    def __init__(self, n: int, pick: int):
        self.n = n
        self.pick = pick
        self.number = self.generatePick(n, pick)
        print("init")
    
    def generatePick(self, n: int, pick: int):
            return random.randint(1, n) if pick is None else pick

    def guess(self, num: int) -> int:
        if num == self.pick:
            return 0
        elif num > self.pick:
            return -1
        else:
            return 1

    def guessNumber(self, n: int) -> int:
        i, j = 0, n
        g = n / 2
        while(True):
            if self.guess(g) == 0:
                return int(g)
            elif self.guess(g) == -1:
                j = g
                g -= (j - i) / 2
            else:
                i = g
                g += (j - i) / 2

    def main(self):
        start = timer()
        print(self.guessNumber(self.n))
        # Function call
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # n, pick = 10, 6 # Output: 6
    # n, pick = 1, 1 # Output: 1
    n, pick = 2, 1 # Output: 1

    sol = Solution(n, pick)
    sol.main()