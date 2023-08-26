from timeit import default_timer as timer
from typing import List, Optional
from pack.TreeNode import TreeNode

class Solution:
    def __init__(self, root):
        self.root = root
        print("init")

    def invertTree(self, root: Optional[TreeNode], invr = None) -> Optional[TreeNode]:
        if root == None: return root
        invr = TreeNode(root.val)
        invr.left = self.invertTree(root.right, invr.left)
        invr.right = self.invertTree(root.left, invr.right)

        return invr

    def main(self):
        invr = self.invertTree(self.root)
        invr.traverse()
        return

if __name__ == "__main__":
    root = TreeNode()
    root.populateFromScratch(16)
    root.traverse()

    # root = None
    sol = Solution(root)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
