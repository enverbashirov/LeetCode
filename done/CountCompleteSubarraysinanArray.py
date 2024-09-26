from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        mp1, mp2 = {}, {}

        for i in nums:
            mp1[i] = mp1.get(i, 0) + 1
        
        i, j, n, ans = 0, 0, len(nums), 0

        while i < n:
            mp2[nums[i]] = mp2.get(nums[i], 0) + 1
            while len(mp2) == len(mp1):
                ans += (n - i)
                mp2[nums[j]] -= 1
                if mp2[nums[j]] == 0:
                    del mp2[nums[j]]
                j += 1
            i += 1
        
        return ans
    
    def main(self):
        start = timer()
        print(self.countCompleteSubarrays(self.nums))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    nums = [1,3,1,2,2] # Output: 4
    # nums = [5,5,5,5] # Output: 10

    sol = Solution(nums)
    sol.main()