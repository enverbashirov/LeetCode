from timeit import default_timer as timer
from typing import List
import numpy as np

class Solution:
    def __init__(self, image, sr, sc, color):
        self.image = image
        self.sr = sr
        self.sc = sc
        self.color = color
        print("init")

    def fill(self, image, sr, sc, color, cur):
        # If sr is less than 0 or greater equals to the length of image...
        # Or, If sc is less than 0 or greater equals to the length of image[0]...
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]): return
        # If image[sr][sc] is not equal to previous color...
        if cur != image[sr][sc]: return
        # Update the image[sr][sc] as a color...
        image[sr][sc] = color
        # Make four recursive calls to the function with (sr-1, sc), (sr+1, sc), (sr, sc-1) and (sr, sc+1)...
        self.fill(image, sr-1, sc, color, cur)
        self.fill(image, sr+1, sc, color, cur)
        self.fill(image, sr, sc-1, color, cur)
        self.fill(image, sr, sc+1, color, cur)
    
    def floodFill(self, image, sr, sc, color):
        # Avoid infinite loop if the new and old colors are the same...
        if image[sr][sc] == color: return image
        # Run the fill function starting at the position given...
        self.fill(image, sr, sc, color, image[sr][sc])
    
        # WRONG SOL: Taking center as starting point and filling 4-dir and 4-diag
        # r, c = len(image), len(image[0])
        # print(r, c)
        # i, j = sr, sc
        # while(i-1 >= 0 and image[sr][sc] == image[i-1][sc]): i-=1; image[i][sc] = color
        # i, j = sr, sc
        # while(i+1 < r and image[sr][sc] == image[i+1][sc]): i+=1; image[i][sc] = color
        # i, j = sr, sc
        # while(j-1 >= 0 and image[sr][sc] == image[sr][j-1]): j-=1; image[sr][j] = color
        # i, j = sr, sc
        # while(j+1 < c and image[sr][sc] == image[sr][j+1]): j+=1; image[sr][j] = color
        # i, j = sr, sc
        # while(i-1 >= 0 and j-1 >= 0 and image[sr][sc] == image[i-1][j-1]): i-=1; j-=1; image[i][j] = color
        # i, j = sr, sc
        # while(i+1 < r and j-1 >= 0 and image[sr][sc] == image[i+1][j-1]): i+=1; j-=1; image[i][j] = color
        # i, j = sr, sc
        # while(i-1 >= 0 and j+1 < c and image[sr][sc] == image[i-1][j+1]): i-=1; j+=1; image[i][j] = color
        # i, j = sr, sc
        # while(i+1 < r and j+1 < c and image[sr][sc] == image[i+1][j+1]): i+=1; j+=1; image[i][j] = color
        # image[sr][sc] = color

        return image
    
    def main(self):
        print(self.floodFill(self.image, self.sr, self.sc, self.color))
        return

if __name__ == "__main__":
    # image = np.ones((5, 5)); sr = 2; sc = 2; color = 2; ans = np.ones((5, 5))
    image = [[1,1,1],[1,1,0],[1,0,1]]; sr = 1; sc = 1; color = 2; ans = [[2,2,2],[2,2,0],[2,0,1]]
    # image = [[0,0,0],[0,0,0]]; sr = 0; sc = 0; color = 0; ans = [[0,0,0],[0,0,0]]

    sol = Solution(image, sr, sc, color)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
