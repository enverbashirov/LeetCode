from timeit import default_timer as timer
from typing import List, Optional
from pack.TreeNode import TreeNode

class Solution:
    def __init__(self, root):
        self.root = root
        print("init")

    # def ceil(self, n):
    #     return int(-1 * n // 1 * -1)

    # def floor(self, n):
    #     return int(n // 1)
    
    def traverse(self, root, arr = [], i = 1):
        if len(arr) < i: arr.append([root.val])
        if len(arr) < i+1 and (root.left or root.right): arr.append([])
        
        if root.left: arr[i].append(root.left.val)
        if root.right: arr[i].append(root.right.val)
        
        if root.left: self.traverse(root.left, arr, i+1)
        if root.right: self.traverse(root.right, arr, i+1)

        return arr

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root: return self.traverse(root, [], 1)
        return []

    def main(self):
        print(self.levelOrder(self.root))
        return

if __name__ == "__main__":
    root = [3,9,20,None,None,15,7] #Output: [[3],[9,20],[15,7]]
    # root = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    # root = [1] #Output: [[1]]
    # root = [] #Output: []

    root = TreeNode().populateFromArr(root)
    # root.display()

    sol = Solution(root)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
