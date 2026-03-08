from timeit import default_timer as timer
from pack.TreeNode import TreeNode
from typing import Optional

class Solution:
    def __init__(self, root, key):
        self.root = root
        self.key = key
        print("init")

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None 
        if root.val == key:
            return self.helper(root)
        
        dummy = root
        while root is not None:
            if root.val > key:
                if root.left is not None and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right is not None and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
        return dummy
    
    def helper(self, root):
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        rightChild = root.right
        lastRight = self.flr(root.left)  # rightmost node in left subtree
        lastRight.right = rightChild
        return root.left
    
    def flr(self, root):
        if root.right is None:
            return root
        return self.flr(root.right)

    def main(self):
        start = timer()
        self.deleteNode(self.root, self.key).traverse()
        # Function call
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    root, key = [5,3,6,2,4,None,7], 3 # Output: [5,4,6,2,null,null,7]
    # root, key = [5,3,6,2,4,None,7], 0 # Output: [5,3,6,2,4,null,7]
    # root, key = [], 0 # Output: []

    sol = Solution(TreeNode().populateFromArr(root), key)
    sol.main()