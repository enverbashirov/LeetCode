from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums):
        self.nums = nums
        print("init")

    def canPartition(self, nums: List[int]) -> bool:
        def rec(i,rsum ):
            if(rsum==0): return True
            if(i==len(nums) or rsum < 0): return False 
            elif(self.dp[i][rsum] != -1 ):
                return self.dp[i][rsum]
            self.dp[i][rsum]= rec(i+1,rsum-nums[i]) or rec(i+1,rsum)
            return self.dp[i][rsum]
        
        
        totalsum = sum(nums)
        if(totalsum%2): return False 
        else: 
            self.dp = [ [-1]*((totalsum//2)+1) for _ in range(len(nums))]
            return rec(0,totalsum//2)

    def main(self):
        print(self.canPartition(self.nums))

if __name__ == "__main__":
    # nums = [1,5,11,5] # Output: true
    nums = [1,2,5,5,11] # Output: true
    # nums = [1,2,3,5,9] # Output: false
    # nums = [1,2,3,5] # Output: false

    sol = Solution(nums)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")