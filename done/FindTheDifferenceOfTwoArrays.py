from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        print("init")
    
    # O(n x m) solution
    # def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    #     set1, set2 = set(nums1), set(nums2)
    #     r1, r2 = [], []
    #     for a in set1:
    #         if a not in set2:
    #             r1.append(a)

    #     for a in set2:
    #         if a not in set1:
    #             r2.append(a)

    #     return [r1, r2]
    
    # O(n x m) again but pythonic way of doing it, slightly more elegant
    # probably slightly waster since set operations are c optimized
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        
        return [list(s1 - s2), list(s2 - s1)] 
    

    def main(self):
        start = timer()
        print(self.findDifference(self.nums1, self.nums2))
        # Function call
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":

    # nums1, nums2 = [1,2,3], [2,4,6] # Output: [[1,3],[4,6]]
    nums1, nums2 = [1,2,3,3], [1,1,2,2] # Output: [[3],[]]
    nums1, nums2 = [1,2,3,3], [1,1,2,2] # Output: [[3],[]]

    sol = Solution(nums1, nums2)
    sol.main()