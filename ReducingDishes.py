from typing import List

class Solution:
    def __init__(self):
        print("init")

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        temp = [0] * len(satisfaction)
        output = 0
        satisfaction.sort()
        print(satisfaction)
        for i, _ in enumerate(satisfaction):
            print(satisfaction[i:])
            for j, s in enumerate(satisfaction[i:]): 
                temp[i] += s*(j+1)
            print(i, temp[i])

        print(temp)
        for s in temp: 
            if s > output: 
                output = s

        return output

    def main(self):
        satisfaction = [4,3,2]
        print(sol.maxSatisfaction(satisfaction))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
