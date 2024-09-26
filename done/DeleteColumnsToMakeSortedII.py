from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, strs):
        self.strs = strs

    def minDeletionSize(self, strs: List[str]) -> int:

        tpse, n, m = zip(*strs), len(strs), len(strs[0])
        strs = [''] * n

        for nxt in tpse:
            temp = [strs[i]+nxt[i] for i in range(n)]
            if temp == sorted(temp): strs = temp
            
        return m - len(strs[0])

    def main(self):
        start = timer()
        print(self.minDeletionSize(self.strs))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # strs = ["ca","bb","ac"] # Output: 1
    strs = ["aaca","aabb","aaac"] # Output: 3
    # strs = ["zyx","wvu","tsr"] # Output: 3
    # strs = ["zyx","wvu","tsr"] # Output: 3

    sol = Solution(strs)
    sol.main()