from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, digits):
        self.digits = digits

    def letterCombinations(self, digits: str) -> List[str]:
        comb = []
        if not digits: return comb

        letters = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
                
        for d in digits:
            current = letters[int(d)-2]
            if comb == []: comb = current; continue
            
            temp = []
            for c1 in current:
                for c2 in comb:
                    temp.append(c2+c1)
            comb = temp
            # print(comb)

        return comb

    def main(self):
        start = timer()
        print(self.letterCombinations(self.digits))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    digits = "23" # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    # digits = "" # Output: []
    # digits = "2" # Output: ["a","b","c"]

    sol = Solution(digits)
    sol.main()