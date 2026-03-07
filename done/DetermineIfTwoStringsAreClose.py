from timeit import default_timer as timer
from typing import Counter, List

class Solution:
    def __init__(self, word1: str, word2: str):
        self.word1 = word1
        self.word2 = word2
        print("init")

    def closeStrings(self, word1: str, word2: str) -> bool:
        frequency_word1 = Counter(word1)
        frequency_word2 = Counter(word2)

        sorted_values_word1 = sorted(frequency_word1.values())
        sorted_values_word2 = sorted(frequency_word2.values())
      
        keys_match = set(frequency_word1.keys()) == set(frequency_word2.keys())

        return sorted_values_word1 == sorted_values_word2 and keys_match

    def main(self):
        start = timer()
        print(self.closeStrings(self.word1, self.word2))
        # Function call
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    
    # word1, word2 = "abc", "bca" # Output: true
    # word1, word2 = "a", "aa" # Output: false
    word1, word2 = "cabbba", "abbccc" # Output

    sol = Solution(word1, word2)
    sol.main()