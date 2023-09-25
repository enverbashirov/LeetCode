from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, grid):
        self.grid = grid
        print("init")


    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans

    def main(self):
        print(self.numIslands(self.grid))
        return

if __name__ == "__main__":
    grid = [["1","1","1","1","0"],  ["1","1","0","1","0"],  ["1","1","0","0","0"],  ["0","0","0","0","0"]] #Output: 1
    # grid = [["1","1","0","0","0"],  ["1","1","0","0","0"],  ["0","0","1","0","0"],  ["0","0","0","1","1"]] #Output: 3

    sol = Solution(grid)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
