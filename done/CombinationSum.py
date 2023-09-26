from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, candidates, target):
        self.candidates = candidates
        self.target = target
        print("init")

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def dfs(cur, cur_sum, idx):                       # try out each possible cases
            if cur_sum > target: return                   # this is the case, cur_sum will never equal to target
            if cur_sum == target: ans.append(cur); return # if equal, add to `ans`
            for i in range(idx, n): dfs(cur + [candidates[i]], cur_sum + candidates[i], i) # DFS
            
        dfs([], 0, 0)
        return ans    

    def main(self):
        print(self.combinationSum(self.candidates, self.target))

if __name__ == "__main__":
    candidates = [2,3,6,7]; target = 7 #Output: [[2,2,3],[7]]
    # candidates = [2,3,5]; target = 8 #Output: [[2,2,2,2],[2,3,3],[3,5]]
    # candidates = [2]; target = 1 #Output: []

    sol = Solution(candidates, target)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
