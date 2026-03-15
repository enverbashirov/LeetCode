from timeit import default_timer as timer

class Solution:
    def __init__(self, p, q):
        p = self.p
        q = self.q
        print("init")

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False
    
    def main(self):
        start = timer()
        print(self.isSameTree())
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    sol = Solution()
    sol.main()