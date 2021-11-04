from timeit import default_timer as timer

class Solution:
    def __init__(self):
        print("init")

    def main(self):
        return

if __name__ == "__main__":
    sol = Solution()
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
