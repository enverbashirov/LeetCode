from timeit import default_timer as timer
from typing import List, Optional
from pack.TreeNode import TreeNode
import collections

class Solution:
    def __init__(self, root):
        self.root = root
        print("init")

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=collections.deque()
        q.append(root)
        
        while q:
            qLen=len(q)
            rightSide=None
            for i in range(qLen):
                node=q.popleft()
                if node:
                    rightSide=node      #This line make's note of the most recent right Side node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightSide:
                res.append(rightSide.val)
        return res
        
    def main(self):
        start = timer()
        if self.root: self.root.display()
        print(self.rightSideView(self.root))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # root = [1,2,3,None,5,None,4] # Output: [1,3,4]
    root = [1,2,3,4,5,6,7] # Output: [1,3,7,15,18]
    # root = [1,2,3,4,5,None,None,8,None,None,None,12,13,None,None] # Output: [1,3,7,15,18]
    # root = [1,None,3] # Output: [1,3]
    # root = [] # Output: []

    sol = Solution(TreeNode().populateFromArr(root))
    sol.main()