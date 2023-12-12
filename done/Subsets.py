from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subb(0,nums,[],[]) #recursion

    def subb(self, i,nums,l,ans):
        if i==len(nums):#if we are at the last element of the array
            if l not in ans:
                ans.append(l)#if l is not in ans then we will apppend l to nums
            return
        #we have 2 choices here one to choose the element or not to choose a element
        self.subb(i+1,nums,l+[nums[i]],ans)#choosing an element append the ith element to l and send i+1 to recursion
        self.subb(i+1,nums,l,ans)#not choosing an element we will just send i+1 to the recursion
        return ans
    
    def main(self):
        start = timer()
        print(self.subsets(self.nums))
        print(f"{timer() - start:.20f}")

    # [[],
    # [1],[2],[3],[4],
    # [1,2],[1,3],[1,4],[2,3],[2,4],[3,4],
    # [1,2,3],[1,2,4],[1,3,4],[2,3,4],
    # [1,2,3,4]]



if __name__ == "__main__":
    nums = [1,2,3,4] # Output: [[],[1],[2],[3],[4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[1,2,3],[1,2,4],[1,3,4],[2,3,4],[1,2,3,4]]
    # nums = [1,2,3] # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    # nums = [1,2] # Output: [[],[1],[2],[1,2]]
    # nums = [0] # Output: [[],[0]]

    sol = Solution(nums)
    sol.main()