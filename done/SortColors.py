from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums):
        self.nums = nums
        print("init")

    def sortColors(self, nums: List[int]) -> None:
        # Do not return anything, modify nums in-place instead.
        # Order: [0]red -> [1]white -> [2]blue
        nums[:] = [0]*nums.count(0) + [1]*nums.count(1) + [2]*nums.count(2)

    def main(self):
        self.sortColors(self.nums)
        print(self.nums)
        return

if __name__ == "__main__":
    nums = [1,1,0] # [0,0,1,1,2,2]
    # nums = [2,0,1] # [0,1,2]

    sol = Solution(nums)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")