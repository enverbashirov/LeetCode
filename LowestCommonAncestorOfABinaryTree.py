from timeit import default_timer as timer
from typing import List
from pack.TreeNode import TreeNode
import queue

class Solution:
    def __init__(self, root, p, q):
        self.root = TreeNode().populateFromArr(root)
        self.p = p
        self.q = q
        print("init")

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l or r

    def main(self):
        print(self.lowestCommonAncestor(self.root, self.p, self.q))
        return

if __name__ == "__main__":
    root = [3,5,1,6,2,0,8,None,None,7,4]; p = 5; q = 1 #Output: 3
    # root = [3,5,1,6,2,0,8,None,None,7,4]; p = 5; q = 4 #Output: 5
    # root = [1,2], p = 1, q = 2 #Output: 1

    sol = Solution(root, p, q)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")

    
