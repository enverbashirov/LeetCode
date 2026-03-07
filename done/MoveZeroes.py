from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        print("init")

    def moveZeroes(self, nums: List[int]) -> None:        
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.extend(([nums.pop(nums.index(0)) for _ in range(nums.count(0))]))

    def main(self):
        start = timer()
        self.moveZeroes(self.nums)
        print(self.nums)
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # nums = [0,1,0,3,12] # Output: [1,3,12,0,0]
    # nums = [0] # Output: [0]
    nums = [0,0,1] # Output: [1, 0, 0]

    sol = Solution(nums)

    sol.main()