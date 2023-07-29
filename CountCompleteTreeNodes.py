from timeit import default_timer as timer
from typing import Optional
from time import sleep

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def populate(self, i, n, node):
        node.val = i

        if n >= (i*2): node.left = self.populate(i*2, n, TreeNode())
        if n >= (i*2)+1: node.right = self.populate((i*2)+1, n, TreeNode())

        return node

    def traverse(self, node=None):
        print(node.val, end = ' ')
        if node.left: self.traverse(node.left)
        if node.right: self.traverse(node.right)
    
class Solution:
    def __init__(self):
        print("init")

    def computeLR(self, v, d):
        l = v * (2 ** d)
        r = l + ((2 ** d) - 1)
        return l, r

    def computeMid(self, l, r):
        return int((l + r) / 2)

    def findLR(self, r, toLeft=True):
        d = 0
        while(toLeft and r.left): r = r.left; d += 1
        while(~toLeft and r.right): r = r.right; d += 1

        return r, d

    def checkNode(self, r, v, d):
        exists = True
        while(exists):
            sleep(0.2)
            lmax = (r.val + 1) * (2 ** (d - 1)) + ((2 ** (d - 1)) - 1)
            rmin = (r.val + 2) * (2 ** (d - 1))
            if v <= lmax: 
                if r.left: r = r.left
                else: exists = ~exists
            elif v >= rmin:
                if r.right: r = r.right
                else: exists = ~exists
            print(lmax, rmin, r.val, v)
            if r.val >= v: return True
        return False

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root.val == 0: return 0

        l, dl = self.findLR(root, True)
        r, dr = self.findLR(root, False)
        cl, cr = self.computeLR(root.val, dl)
        mid = self.computeMid(cl, cr)

        print(self.checkNode(root, 7, dl))

        print(l.val, cl, dl, r.val, cr, dr, mid)
        
        # while(dl != dr): 

            
            

        return r

if __name__ == "__main__":
    sol = Solution()
    root = [1,2,3,4,5,6]
    # root = []
    ans = root[-1] if root else 0
    
    # Populate Tree and Visualize after for proof
    root = TreeNode().populate(1, len(root), TreeNode()) if root != [] else TreeNode(); print()
    root.traverse(root); print()

    # Solve the problem
    start = timer()
    a = sol.countNodes(root)
    print(a == ans, a)
    print(f"{timer() - start:.20f}")
