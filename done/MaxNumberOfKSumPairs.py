from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums: List[int], k: int):
        self.nums = nums
        self.k = k
        print("init")

    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        r, i, j = 0, 0, len(nums) - 1
        while i < j: 
            print(nums, r, i, j)
            if nums[i] + nums[j] == k: 
                r += 1
                i += 1
                j -= 1
            elif k - (nums[i] + nums[j]) > 0:
                i += 1
            else:
                j -= 1

        print(nums, r, i, j)
        
        return r

    def main(self):
        start = timer()
        print(self.maxOperations(self.nums, self.k))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # nums, k = [1,2,3,4], 5 # Output: 2
    nums, k = [3,1,3,4,3], 6 # Output: 1

    sol = Solution(nums, k)
    sol.main()