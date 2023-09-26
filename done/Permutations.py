from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums):
        self.nums = nums
        print("init")

    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        return res
    
    def backtracking(self,res,visited,subset,nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res,visited,subset+[nums[i]],nums)
                visited.remove(i)
    
    def main(self):
        print(self.permute(self.nums))
        return

if __name__ == "__main__":
    nums = [1,2,3] #Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    # nums = [0,1] #Output: [[0,1],[1,0]]
    # nums = [1] #Output: [[1]]

    sol = Solution(nums)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
