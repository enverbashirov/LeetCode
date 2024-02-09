from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers)-1

        for i, n in enumerate(numbers):
            if numbers[low] + numbers[high] == target: return [low+1, high+1]
            else:
                if numbers[low] + numbers[high] < target: low += 1
                else: high -= 1

    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # if len(numbers) == 2: return [1, 2]
        # for i, n in enumerate(numbers[:-1]):
        #     if (target - n) in numbers: return [i+1, numbers[i+1:].index(target-n)+i+2]

    def main(self):
        start = timer()
        print(self.twoSum(self.numbers, self.target))
        # Function call
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # numbers = [2,7,11,15]; target = 9 # Output: [1,2]
    # numbers = [0,0,3,4]; target = 0 # Output: [1,2]
    # numbers = [2,3,4]; target = 6 # Output: [1,3]
    # numbers = [-1,0]; target = -1 # Output: [1,2]
    # numbers = [-1,0]; target = -1
    numbers = [5,25,75]; target = 100

    sol = Solution(numbers, target)
    sol.main()