from timeit import default_timer as timer
from typing import List
# from time import sleep

class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        print("init")

    def search(self, nums: List[int], target: int) -> int:
        r = [0, len(nums)] # search range
        m = int(sum(r) / 2)
        
        if r[1] == 1 & nums[r[1]-1] == target: return True 

        while(1):
            if nums[m] == target: return m
            if nums[m] > target: 
                r[1] = m
            elif nums[m] < target: 
                r[0] = m
            # print(m, r, int(sum(r)/ 2))
            if m == int(sum(r) / 2): return -1
            m = int(sum(r) / 2)
            # sleep(1)

    def main(self):
        print(self.search(self.nums, self.target))
        return

if __name__ == "__main__":
    # nums = [-1,0,3,5,9,12]; target = 9
    nums = [-1,0,3,5,9,12]; target = 2
    # nums = [-1]; target = 2

    sol = Solution(nums, target)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
