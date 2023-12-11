from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, matrix):
        self.matrix = matrix

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix[0]), len(matrix)
        ans = []
        while(n >= 1 or m >= 1):
            if m >= 1:
                ans.extend(matrix[0]) # top left -> top right
                matrix = matrix[1:]      
                print(ans, matrix, n, m)
                m -= 1
            if n >= 1:
                ans.extend([row[-1] for row in matrix]) # top right -> bottom right
                matrix = [row[:-1] for row in matrix]
                print(ans, matrix, n, m)
                n -= 1
            if m >= 1:
                ans.extend(reversed(matrix[-1])) # bottom right -> bottom left
                matrix = matrix[:-1]
                print(ans, matrix, n, m)
                m -= 1
            if n >= 1:
                ans.extend(reversed([row[0] for row in matrix])) # bottom left -> top left
                matrix = [row[1:] for row in matrix]
                print(ans, matrix, n, m)
                n -= 1
           
        return ans
        
    def main(self):
        print(self.spiralOrder(matrix))

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]] # Output: [1,2,3,6,9,8,7,4,5]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]] # Output: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

    sol = Solution(matrix)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")