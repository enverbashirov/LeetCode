from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, intervals):
        self.intervals = intervals
        print("init")

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = [intervals[0]]
        for i in intervals:
            if ans[-1][0] <= i[0] and ans[-1][1] >= i[0]: 
                if ans[-1][1] <= i[1]: ans[-1][1] = i[1]
            else: ans.append(i)

        return ans

    def main(self):
        print(self.merge(self.intervals))
        return

if __name__ == "__main__":
    # intervals = [[1,4],[0,4]] # [[0, 4]]
    intervals = [[1,2],[5,6],[-1,0],[-1,5],[10,50],[-6,9]]
    # intervals = [[1,3],[2,6],[8,10],[15,18]] #Output: [[1,6],[8,10],[15,18]]
    # intervals = [[1,3],[2,6],[8,10],[10,18],[11,19]] #Output: [[1,6],[8,10],[15,18]]
    # intervals = [[1,4],[4,5]] #Output: [[1,5]]

    sol = Solution(intervals)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
