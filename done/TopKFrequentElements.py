from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
        print("init")

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = []
        d = dict.fromkeys(set(nums), 0)
        for c in nums:
            d[c] += 1

        while k > 0:
            k -= 1
            key = max(d, key=d.get)
            r.append(int(key))
            d.pop(key)
        
        return r

    def main(self):
        start = timer()
        # Function call
        print(self.topKFrequent(self.nums, self.k))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # nums = [1,1,1,2,2,3]; k = 2 # Output: [1,2]
    # nums = [1]; k = 1 # Output: [1]
    # nums = [1,2,1,2,1,2,3,1,3,2]; k = 2 # Output: [1,2]
    # nums = [1, 1]; k = 2 # Output: [1,2]
    nums = [4,1,-1,2,-1,2,3]; k = 2 # Output: [2,-1]
    sol = Solution(nums, k)
    sol.main()
