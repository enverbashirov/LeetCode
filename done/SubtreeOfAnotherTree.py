from timeit import default_timer as timer
from pack.TreeNode import TreeNode
from typing import Optional

class Solution:
    def __init__(self, root, subRoot):
        self.root = root
        self.subRoot = subRoot
        print("init")
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "N"
            return f"({node.val},{serialize(node.left)},{serialize(node.right)})"
        
        rootSerialized = serialize(root)
        subRootSerialized = serialize(subRoot)
        return subRootSerialized in rootSerialized
    
    def main(self):
        start = timer()
        # Function call
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    sol = Solution()
    sol.main()