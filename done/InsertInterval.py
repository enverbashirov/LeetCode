from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, intervals, newInterval):
        self.intervals = intervals
        self.newInterval = newInterval
        print("init")

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, j = -2, -2
        if intervals == []: return [newInterval]
        if intervals[0][0] > newInterval[1]: return [newInterval] + intervals

        for idx, [s, e] in enumerate(intervals):
            if i == -2 and e >= newInterval[0]: i = idx
            if s <= newInterval[1]: j = idx

        s = min(newInterval[0], intervals[i][0]) if i >= 0 else newInterval[0]
        e = max(newInterval[1], intervals[j][1]) if j >= 0 else newInterval[1]
        newInterval = [s, e]

        if i == -2: return intervals + [newInterval]
        if j == -2: return intervals[:i] + [newInterval]
        return intervals[:i] + [newInterval] + intervals[j+1:]

    def main(self):
        print(self.insert(self.intervals, self.newInterval))
        return

if __name__ == "__main__":
    intervals = []; newInterval = [4,7] #Output: [[4,7]]
    # intervals = [[1,3]]; newInterval = [4,7] #Output: [[1,3],[4,7]]
    # intervals = [[1,4]]; newInterval = [4,7] #Output: [[1,7]]
    # intervals = [[1,3], [8,9]]; newInterval = [4,7] #Output: [[1,3],[4,7],[8,9]]
    # intervals = [[1,3], [7,9]]; newInterval = [4,7] #Output: [[1,3],[4,9]]
    # intervals = [[8,9]]; newInterval = [4,7] #Output: [[4,7],[8,9]]
    # intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]; newInterval = [4,8] #Output: [[1,2],[3,10],[12,16]]
    
    sol = Solution(intervals, newInterval)

    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
