from timeit import default_timer as timer

class Solution:
    def __init__(self, s: str):
        print("init")
        self.s = s

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)

        r = 1
        i, j = 0, 1
        while i + r < len(s):
            j = i+r
            while j <= len(s):
                if len(set(s[i:j])) < len(s[i:j]): break
                if len(set(s[i:j])) > r:
                    r = len(set(s[i:j]))
                    # print(s[i:j])
                j += 1
            i += 1
        return r

    def main(self):
        start = timer()
        # Function call
        print(self.lengthOfLongestSubstring(self.s))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # s = "abcabcbb" # Output: 3
    # s = "bbbbb" # Output: 1
    s = "pwwkew" # Output: 3

    print(s)
    sol = Solution(s)
    sol.main()

