from timeit import default_timer as timer
from typing import List
import numpy as np

class Solution:
    def __init__(self):
        print("init")

    def rob(self, nums):
        if len(nums) == 1: return nums[0]
        def subrob(subnums):
            last, now = 0, 0
            for i in subnums: 
                last, now = now, max(last + i, now)
                print(i, last, now)
            return now
        return max(subrob(nums[:-1]), subrob(nums[1:]))

    # def robnext(self, nums:List[int], i:int, sum:int) -> int:
    #     if i >= len(nums):
    #         print('Final', i, sum, end='\r')
    #         return sum
    #     # print('Mid  ', i, sum + nums[i])
    #     return max(self.robnext(nums, i+2, sum + nums[i]), self.robnext(nums, i+3, sum + nums[i]))
    
    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) <= 3:
    #         return max(nums)

    #     return max(self.robnext(nums[:-1], 0, 0), self.robnext(nums, 1, 0), self.robnext(nums, 2, 0))
    
    def main(self):
        # nums = [2,3,2]; ans = 3
        # nums = [1,2,3]; ans = 3
        # nums = [1,5,1,1,5,1]; ans = 10
        # nums = [1,5,1,5,6,5,1]; ans = 15
        nums = [1,5,1,5,6,5,20]; ans = 31
        # nums = [1,2,3,1]; ans = 4
        # nums = [226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]; ans = 0
        a = self.rob(nums)
        print(a == ans, a)

if __name__ == "__main__":
    sol = Solution()
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
