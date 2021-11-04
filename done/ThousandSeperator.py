from timeit import default_timer as timer

class Solution:
    def __init__(self):
        print("init")

    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        d = 3
        c = 0
        rem = len(s) % d if len(s) % d > 0 else 3

        for i in range(rem, len(s), d):
            s = s[:i+c] + "." + s[i+c:]
            c += 1

        return s
        
    def main(self):
        n = 1234567890
        print(self.thousandSeparator(n))
        return

if __name__ == "__main__":
    sol = Solution()
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
