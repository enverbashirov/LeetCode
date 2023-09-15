from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums):
        self.nums = nums
        print("init")

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)

    def main(self):
        print(self.productExceptSelf(self.nums))
        return

if __name__ == "__main__":
    nums = [1,2,3,4] #Output: [24,12,8,6]
    # nums = [-1,1,0,-3,3] #Output: [0,0,9,0,0]

    sol = Solution(nums)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
