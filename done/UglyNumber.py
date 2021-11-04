from timeit import default_timer as timer

class Solution:
    def __init__(self):
        print("init")

    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        while n > 1:
            print(n)
            if n%2 == 0:
                n /= 2
            elif n%3 == 0:
                n /= 3
            elif n%5 == 0:
                n /= 5
            else:
                return False
        return True

    def main(self):
        n = -2147483648
        print(self.isUgly(n))
        # return self.isUgly(n)

if __name__ == "__main__":
    sol = Solution()
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
