from timeit import default_timer as timer
from pack.TreeNode import TreeNode
from typing import Optional

class Solution:
    def __init__(self, root: Optional[TreeNode] = None):
        self.root = root
        print("init")

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level_sums = {}
        
        def dfs(node, level):
            if not node:
                return
            
            if level not in level_sums:
                level_sums[level] = 0
            level_sums[level] += node.val
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 1)
        
        # Find level with max sum
        max_level = max(level_sums, key=level_sums.get)
        return max_level

    def main(self):
        start = timer()
        print(self.maxLevelSum(self.root))
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # root = [1,7,0,7,-8,None,None] # Output: 2
    root = [989,None,10250,98693,-89388,None,None,None,-32127] # Output: 2

    sol = Solution(TreeNode().populateFromArr(root))
    sol.main()