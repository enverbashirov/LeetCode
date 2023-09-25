from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        print("init")

    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        
        while low<=high:
            mid = (low+high)//2

            if target == nums[mid]:
                return mid

            # check if left half is sorted
            elif nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1

            # Otherwise, right half is sorted
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1
    
        # Not O(log n) but Simple Answer
        # if target not in nums: return -1
        # return nums.index(target)


    def main(self):
        print(self.search(self.nums, self.target))
        return

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]; target = 0 #Output: 4
    # nums = [4,5,6,7,8,0,1,2,3]; target = 0
    # nums = [4,5,6,7,0,1,2]; target = 3 #Output: -1
    # nums = [1]; target = 0 #Output: -1

    sol = Solution(nums, target)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
