from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums):
        self.nums = nums
        print("init")

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid = left + 1
            right = len(nums) - 1

            while mid < right:
                summ = nums[left] + nums[mid] + nums[right]
                if summ < 0:
                    mid += 1
                elif summ > 0:
                    right -= 1
                else:
                    result.append([nums[left],nums[mid],nums[right]]) 
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid+=1
                    while mid < right and nums[right] == nums[right-1]:
                        right -= 1

                    mid +=1
                    right -= 1
        return result

        # Too Slow
        # nums.sort()
        # ans = []
        # for i, n in enumerate(nums[:len(nums)-2]):
        #     for j in range(i+1,len(nums)-1):
        #         a = nums[j]
        #         if [n, a, (0-(n+a))] not in ans and (0-(n+a)) in nums[j+1:]: 
        #             ans.append([n, a, (0-(n+a))])
        #         if ((n+a)) > nums[-1]: break
        # return ans
        
    def main(self):
        print(self.threeSum(self.nums))
        return

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4] # [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
    # nums = [-1,0,1,2,-1,-4] #Output: [[-1,-1,2],[-1,0,1]]
    # nums = [0,1,1] #Output: []
    # nums = [0,0,0] #Output: [[0,0,0]]

    sol = Solution(nums)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
