from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums):
        self.nums = nums
        print("init")

    def majorityElement(self, nums: List[int]) -> int:
        # Best
        # If there exists an int with more than half of the total
        # Than when sorted, value on the middle should be that int
        nums.sort()
        return nums[len(nums)//2]

        # # Better than worst
        # sn = set(nums)
        # for n in sn:
        #     if nums.count(n) > len(nums) / 2:
        #         return n
        # return 0
    
    def main(self):
        print(self.majorityElement(self.nums))
        return

if __name__ == "__main__":
    # nums = [3,2,3] # 3
    nums = [2,2,1,1,1,2,2] # 
    
    sol = Solution(nums)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
