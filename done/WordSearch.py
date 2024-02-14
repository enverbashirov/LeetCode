from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, board, word):
        self.board = board
        self.word = word

    # m == board.length
    # n = board[i].length
    # 1 <= m, n <= 6
    # 1 <= word.length <= 15
    # board and word consists of only lowercase and uppercase English letters.
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def check_neighbors(i, j, word_index):
            if word_index == len(word):
                return True  # Word found

            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[word_index]:
                return False  # Out of bounds or character mismatch

            # Mark the current cell as visited
            temp = board[i][j]
            board[i][j] = "#"  # Using "#" to mark visited cells

            # Explore neighboring cells
            result = check_neighbors(i + 1, j, word_index + 1) or \
                    check_neighbors(i - 1, j, word_index + 1) or \
                    check_neighbors(i, j + 1, word_index + 1) or \
                    check_neighbors(i, j - 1, word_index + 1)

            # Restore the original character
            board[i][j] = temp

            return result

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if check_neighbors(i, j, 0):
                        return True

        return False
    
    def main(self):
        start = timer()
        print(self.exist(self.board, self.word))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "ABCCED" # Output: true
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "ABCCEK" # Output: true
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "SEE" # Output: true
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "ABCB" # Output: false
    board = [["A"]]; word = "A" # Output: true

    sol = Solution(board, word)
    sol.main()