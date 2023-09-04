from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, points, k):
        self.points = points
        self.k = k
        print("init")

    def distance(self, x1, y1, x2 = 0, y2 = 0):
        return abs(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [self.distance(p[0], p[1]) for p in points]
        vals = dist[:k]
        inds = list(range(0,k))

        for i in range(k, len(dist)):
            if dist[i] < max(vals):
                t = vals.index(max(vals))
                vals[t] = dist[i]
                inds[t] = i

        points = [points[i] for i in inds]

        return points

    def main(self):
        print(self.kClosest(self.points, self.k))
        return

if __name__ == "__main__":
    # points = [[1,3],[-2,2]]; k = 1 #Output: [[-2,2]]
    # points = [[3,3],[5,-1],[-2,4]]; k = 2 #Output: [[3,3],[-2,4]]
    # points = [[3, 0],[0,5],[-2,4]]; k = 2
    points = [[0,1],[1,0]]; k = 2

    sol = Solution(points, k)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
