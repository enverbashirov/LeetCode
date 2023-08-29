# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def populateFromScratch(self, n): # Binary Search Tree (1 to n)
        if n >= (self.val * 2):     self.left = TreeNode(self.val*2).populateFromScratch(n)
        if n >= (self.val * 2) + 1: self.right = TreeNode(self.val * 2 + 1).populateFromScratch(n)
        return self
    
    def populateFromArr(self, arr, i = 0): # Binary Tree (filled according to arr)
        if len(arr) > i: self.val = arr[i]
        if len(arr) > (((i+1)*2)-1): self.left = TreeNode(None).populateFromArr(arr, (((i+1)*2)-1))
        if len(arr) > (((i+1)*2)): self.right = TreeNode(None).populateFromArr(arr, (((i+1)*2)))
        return self

    def traverse(self):
        print(self.val, end = ' ')
        if self.left: self.left.traverse()
        if self.right: self.right.traverse()