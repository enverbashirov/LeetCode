from logging import root
from timeit import default_timer as timer
from typing import List
from pack.TreeNode import TreeNode
from typing import Optional

class Solution:
    def __init__(self, root, val):
        self.root = root
        self.val = val
        print("init")

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root

        while node:
            if node.val == val:
                break
            if node.val > val:
                node = node.left
            else:
                node = node.right

        return node


    def main(self):
        start = timer()
        self.searchBST(self.root, self.val).traverse()
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # root, val = [4,2,7,1,3], 2 # Output: [2,1,3]
    root, val = [4,2,7,1,3], 5 # Output: []


    sol = Solution(TreeNode().populateFromArr(root), val)
    sol.main()