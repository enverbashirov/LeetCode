from typing import List
from timeit import default_timer as timer

class Solution:
    def __init__(self):
        print("init")

    # def maxProduct(self, nums: List[int]) -> int:
    #     x, y = 1, 1
    #     for i in nums:
    #         if i >= x:
    #             y = x
    #             x = i
    #         elif i > y:
    #             y = i

    #     return (x-1) * (y-1)

    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        l = nums.__len__()
        return (nums[l-1]-1) * (nums[l-2]-1)
        
    def main(self):
        nums = [10,2,5,2]
        print(nums)
        print(self.maxProduct(nums))
        return 

if __name__ == "__main__":
    sol = Solution()
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
