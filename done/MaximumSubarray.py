from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums):
        self.nums = nums
        print("init")

    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum
        
    def main(self):
        print(self.maxSubArray(self.nums))
        return

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4] #Output: 6
    # nums = [1] #Output: 1
    # nums = [5,4,-1,7,8] #Output: 23

    sol = Solution(nums)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
