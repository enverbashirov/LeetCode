from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums):
        self.nums = nums
        print("init")

    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True

        # Sol 1
        # nums.sort()
        # while len(nums) > 1:
        #     if nums[0] == nums[1]:
        #         return True
        #     # print(nums)
        #     nums = nums[1:]
        # return False

    def main(self):
        print(self.containsDuplicate(self.nums))
        return

if __name__ == "__main__":
    # nums = [1,2,3,1] #Output: true
    # nums = [1,2,3,4] #Output: false
    # nums = [1,1,1,3,3,4,3,2,4,2] #Output: true
    nums = [1] # False
    # nums = [] # False

    sol = Solution(nums)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
