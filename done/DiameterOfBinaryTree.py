from timeit import default_timer as timer
from typing import List, Optional
from pack.TreeNode import TreeNode

class Solution:
    def __init__(self, root):
        self.root = root
        print("init")

    def diam(self, root):
        ll, lr, lc, rl, rr, rc = 0, 0, 0, 0, 0, 0
        if root.left: 
            ll, lr, lc = self.diam(root.left); ll += 1; lr += 1
        if root.right: 
            rl, rr, rc = self.diam(root.right); rl += 1; rr += 1
        l = max(ll, lr)
        r = max(rl, rr)
        c = max(lc, rc, l+r)
        print(l, ll, lr, lc, r, rl, rr, rc, c)
        return l, r, c

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        c = 0
        _, _, c = self.diam(root)
        return c
            
    def main(self):
        print(self.diameterOfBinaryTree(self.root))
        return

if __name__ == "__main__":
    # root = [1,2,3,4,5] # 3
    # root = [1,2] # 1
    root = TreeNode().populateFromArr([1, 2, 3, 4, 5, None, None, 8, 9, None, 10]) # 

    # root = TreeNode().populateFromScratch(root[-1])
    # root = TreeNode().populateFromScratch(15)
    root.traverse()

    sol = Solution(root)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
