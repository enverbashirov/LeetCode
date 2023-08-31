# Definition for singly-linked list.

class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None

    def populateFromArr(self, arr):
        if len(arr) > 0:
            self.val = arr[0]
        if len(arr) > 1:
            self.next = ListNode().populateFromArr(arr[1:])
        return self
    
    def traverse(self):
        print(self.val, end=' ')
        if self.next: self.next.traverse()
        
