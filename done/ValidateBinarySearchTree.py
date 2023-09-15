from timeit import default_timer as timer
from typing import List, Optional
from pack.TreeNode import TreeNode

class Solution:
    def __init__(self, root):
        self.root = root
        print("init")

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def BST(root,mx,mi):
            if not root:
                return True
            elif root.val>=mx or root.val<=mi:
                return False
            else:
                return BST(root.left,root.val,mi) and BST(root.right,mx,root.val)
        return BST(root,float('inf'),float('-inf'))

    def main(self):
        print(self.isValidBST(self.root))
        return

if __name__ == "__main__":
    root = [2,1,3] #True
    # root = [5,1,4,None,None,3,6] # False

    root = TreeNode().populateFromArr(root)

    sol = Solution(root)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
