from timeit import default_timer as timer
from typing import List
from pprint import pprint

class Solution:
    def __init__(self, height):
        self.height = height

    def trap(self, height: List[int]) -> int:
        water = 0 
        for i in range(1, len(height)):
            min_height = min( max(height[0:i]), max(height[i:len(height)]))
            if((min_height - height[i]) > 0):
                water += (min_height - height[i])
        return water
        
    def main(self):
        start = timer()
        print(self.trap(self.height))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1] # Output: 6
    # height = [0,5,4,3,0,3,0] # Output: 3
    # height = [4,2,0,3,2,5] # Output: 9
    
    sol = Solution(height)
    sol.main()