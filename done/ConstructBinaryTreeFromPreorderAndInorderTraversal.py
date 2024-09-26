from timeit import default_timer as timer
from typing import List, Optional
from pack.TreeNode import TreeNode

class Solution:
    def __init__(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
    
    # Inorder => Left, Root, Right.
    # Preorder => Root, Left, Right.
    def buildTree(self, preorder, inorder):
        if inorder:
            i = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[i])
            root.left = self.buildTree(preorder, inorder[:i])
            root.right = self.buildTree(preorder, inorder[i+1:])
			
            return root

        
    def main(self):
        start = timer()
        self.buildTree(self.preorder, self.inorder).display()
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    preorder = [3,9,20,15,7]; inorder = [9,3,15,20,7] # Output: [3,9,20,null,null,15,7]
    # preorder = [-1]; inorder = [-1] # Output: [-1]
    sol = Solution(preorder, inorder)
    sol.main()