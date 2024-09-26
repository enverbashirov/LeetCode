from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, s, k):
        self.s = s
        self.k = k

    def main(self):
        start = timer()
        print(self.minimumPartition(s, k))
        print(f"{timer() - start:.20f}")
    
    def minimumPartition(self, s: str, k: int) -> int:
        ans = 0
        subs = ''
        if k < 10 and int(max(s)) > k: return -1

        for i, c in enumerate(s):
            subs += c
            print(s, ans, subs)
            if int(subs) > k:
                ans += 1
                subs = c
        ans += 1
                
        return ans
    
    
if __name__ == "__main__":
    # s = "165462"; k = 60 # Output: 4
    # s = "199999"; k = 200 # Output: 4
    s = "238182"; k = 5 # Output: -1

    sol = Solution(s, k)
    sol.main()