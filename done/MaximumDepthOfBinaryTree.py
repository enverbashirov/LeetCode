from timeit import default_timer as timer
from typing import List, Optional
from pack.TreeNode import TreeNode

class Solution:
    def __init__(self, root):
        self.root = root
        print("init")

    def depth(self, root: Optional[TreeNode]) -> int:
        l, r = 1, 1
        if root.left: l += self.maxDepth(root.left)
        if root.right: r += self.maxDepth(root.right)
        return max(l, r)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return self.depth(root)
    
    def main(self):
        print(self.maxDepth(self.root))
        return

if __name__ == "__main__":
    # root = [3,9,20,None,None,15,7]
    # root = [1,None,2]
    root = []

    root = TreeNode().populateFromArr(root)
    root.display()

    sol = Solution(root)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
