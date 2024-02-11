from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, height):
        self.height = height
        
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        ans = 0
        while(i < j):
            if min(height[i], height[j]) * (j - i) > ans: 
                ans = min(height[i], height[j]) * (j - i)
            # print(height, i, j, ans)
            
            if height[i] < height[j]: i += 1
            else: j -= 1

        return ans        

    def main(self):
        start = timer()
        self.maxArea(self.height)
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # height = [1,8,6,2,5,4,8,3,7] # Output: 49
    height = [1,2,4,3] # Output: 4
    # height = [1,1] # Output: 1

    sol = Solution(height)
    sol.main()