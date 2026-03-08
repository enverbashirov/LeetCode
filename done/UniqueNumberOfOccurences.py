from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, arr: List):
        self.arr = arr
        print("init")

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for a in arr:
            freq[a] = freq.get(a, 0) + 1

        return len(set(freq)) == len(set(freq.values()))

    def main(self):
        start = timer()
        print(self.uniqueOccurrences(self.arr))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # arr = [1,2,2,1,1,3] # Output: true
    # arr = [1,2] # Output: false
    arr = [-3,0,1,-3,1,1,1,-3,10,0] # Output: true


    sol = Solution(arr)
    sol.main()