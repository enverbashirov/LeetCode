from timeit import default_timer as timer
from typing import List
from pack.TreeNode import TreeNode

class Solution:
    def __init__(self, root: TreeNode(), p, q):
        self.root = root
        self.p = p
        self.q = q
        print("init")

    # def findPQ(self, root, p, q, pv = None, qv = None):
    #     if root.val == p: 
    #         if ~qv: pv = p
    #         elif qv < p: pv = qv
    #         else: pv = p
    #     if root.val == q:
    #         if ~pv: qv = q
    #         elif pv < q: qv = pv
    #         else: qv = q

    #     if qv and pv: return max(qv, pv)

    #     if root.left: pv, qv = self.findPQ(root.left, p, q, pv, qv)
    #     if root.right: pv, qv = self.findPQ(root.right, p, q, pv, qv)

    #     return pv, qv

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pv=p.val
        qv=q.val
        while(root!=None):
            if pv <root.val and qv<root.val:
                root=root.left
            elif pv>root.val and qv>root.val:
                root=root.right
            else:
                return root
        return root
    
    def main(self):
        self.lowestCommonAncestor(self.root, self.p, self.q)
        return

if __name__ == "__main__":
    root = [6,2,8,0,4,7,9,None,None,3,5]; p = 2; q = 8 # ans = 6
    # root = [6,2,8,0,4,7,9,None,None,3,5]; p = 2; q = 4 # ans = 2
    # root = [2,1]; p = 2; q = 1 # ans = 2

    print(root)
    root = TreeNode().populateFromArr(root)
    root.traverse()

    sol = Solution(root, TreeNode(p), TreeNode(q))
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
