from timeit import default_timer as timer
from typing import List
import math as m

class Solution:
    def __init__(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int):
        self.radius = radius
        self.xCenter = xCenter
        self.yCenter = yCenter
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        print("init")

    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xclose = xCenter
        yclose = yCenter
        if not (xclose >= x1 and xclose <= x2):
            if xclose < x1: xclose = x1
            elif xclose > x2: xclose = x2
        if not (yclose >= y1 and yclose <= y2):
            if yclose < y1: yclose = y1
            elif yclose > y2: yclose = y2

        # print(xclose, yclose)

        return abs((xCenter - xclose)**2 + (yCenter - yclose)**2)**.5 <= radius

    def main(self):
        print(self.checkOverlap(self.radius, self.xCenter, self.yCenter, self.x1, self.y1, self.x2, self.y2))
        return

if __name__ == "__main__":
    radius = 1; xCenter = 0; yCenter = 0; x1 = 1; y1 = -1; x2 = 3; y2 = 1 # True
    # radius = 1; xCenter = 1; yCenter = 1; x1 = 1; y1 = -3; x2 = 2; y2 = -1 # False
    # radius = 1; xCenter = 0; yCenter = 0; x1 = -1; y1 = 0; x2 = 0; y2 = 1 # True
    # radius = 4; xCenter = 102; yCenter = 50; x1 = 0; y1 = 0; x2 = 100; y2 = 100 # True
    # radius = 100; xCenter = 0; yCenter = 0; x1 = 99; y1 = 99; x2 = 150; y2 = 150 # False
    sol = Solution(radius, xCenter, yCenter, x1, y1, x2, y2)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")