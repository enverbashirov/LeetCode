# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def populateFromScratch(self, n):
        if n >= (self.val * 2):     self.left = TreeNode(self.val*2).populateFromScratch(n)
        if n >= (self.val * 2) + 1: self.right = TreeNode(self.val * 2 + 1).populateFromScratch(n)
        return self

    def traverse(self):
        print(self.val, end = ' ')
        if self.left: self.left.traverse()
        if self.right: self.right.traverse()