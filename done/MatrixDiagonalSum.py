from timeit import default_timer as timer
from typing import List
import numpy as np

class MatrixDiagonalSum:
    def __init__(self, mat):
        self.mat = mat
        print("init")

    def diagonalSum(self, mat: List[List[int]]) -> int:
        # return np.sum((np.rot90(np.eye(len(mat))) + np.eye(len(mat))).astype(bool).astype(int) * mat)
        
        res = np.sum(np.diagonal(mat) + np.diagonal(np.rot90(mat)))
        if len(mat) % 2 == 1: res -= mat[int(len(mat)/2)][int(len(mat)/2)]
        return res
        
    def main(self):
        return self.diagonalSum(self.mat)

if __name__ == "__main__":
    mat = [[1,2,3], [4,5,6], [7,8,9]]
    # mat = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
    sol = MatrixDiagonalSum(mat)
    start = timer()
    print(sol.main())
    print(f"{timer() - start:.20f}")
