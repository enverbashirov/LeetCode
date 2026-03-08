from timeit import default_timer as timer
from typing import List
from math import ceil
import bisect

class Solution:
    def __init__(self, spells: List[int], potions: List[int], success: int):
        self.spells = spells
        self.potions = potions
        self.success = success
        print("init")


    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        
        for spell in spells:
            # Find minimum potion where spell * potion >= success
            # Equivalent to: potion >= success / spell
            min_potion = (success + spell - 1) // spell  # Ceiling division
            
            # Binary search for first potion >= min_potion
            idx = bisect.bisect_left(potions, min_potion)
            
            # Count valid potions (all potions from idx onwards)
            result.append(len(potions) - idx)
        
        return result


    def main(self):
        start = timer()
        print(self.successfulPairs(self.spells, self.potions, self.success))
        # Function call
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # spells, potions, success = [5,1,3], [1,2,3,4,5], 7 # Output: [4,0,3]
    spells, potions, success = [3,1,2],  [8,5,8], 16 # Output: [2,0,2]

    sol = Solution(spells, potions, success)
    sol.main()