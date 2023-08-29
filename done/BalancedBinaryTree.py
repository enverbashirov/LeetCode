from timeit import default_timer as timer
from typing import List, Optional
from pack.TreeNode import TreeNode


class Solution:
    def __init__(self, root: TreeNode()):
        self.root = root
        print("init")

    def isBalanced(self, root):
        return (self.Height(root) >= 0)
    
    def Height(self, root):
        if root is None:  return 0
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
        return max(leftheight, rightheight) + 1
    
    def main(self):
        self.isBalanced(self.root)
        return

if __name__ == "__main__":
    root = [3,9,20,None,None,15,7] # True
    # root = [1,2,2,3,3,None,None,4,4] # False
    # root = [] # True

    print(root)
    root = TreeNode().populateFromArr(root)
    root.traverse()

    sol = Solution(root)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
