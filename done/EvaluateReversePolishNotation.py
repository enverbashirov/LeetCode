from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, tokens):
        self.tokens = tokens
        print("init")

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            print(t, nums)
            if t == '+': nums = nums[:-2] + [nums[-2] + nums[-1]]; continue
            if t == '-': nums = nums[:-2] + [nums[-2] - nums[-1]]; continue
            if t == '*': nums = nums[:-2] + [nums[-2] * nums[-1]]; continue
            if t == '/': nums = nums[:-2] + [int(nums[-2] / nums[-1])]; continue
            nums.append(int(t))
        return nums[0]
    
    def main(self):
        ans = self.evalRPN(self.tokens)
        print(ans)
        return

if __name__ == "__main__":
    # tokens = ["2","1","+","3","*"] #Output: 9
    # tokens = ["4","13","5","/","+"] #Output: 6
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] #Output: 22
    # tokens = ["2","5","/"] #Output: 0
    # tokens = ["-2","5","/"] #Output: 0
    
    sol = Solution(tokens)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
