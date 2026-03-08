import nt
from timeit import default_timer as timer
from typing import List, Optional
from pack.ListNode import ListNode

class Solution:
    def __init__(self, head: ListNode):
        self.head = head
        print("init")

    def deleteMiddle(self, head):
        # Edge case: single node
        if not head or not head.next:
            return None
        
        # Find node before middle using slow/fast pointers
        slow = head
        fast = head.next.next  # Start fast 2 steps ahead
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Delete middle node
        slow.next = slow.next.next
        return head
                
    def main(self):
        start = timer()
        self.deleteMiddle(self.head)
        ListNode.traverse(self.head)
        # Function call
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    head = [1,3,4,7,1,2,6] # Output: [1,3,4,1,2,6]
    # head = [1,2,3,4] # Output: [1,2,4]
    # head = [2,1] # Output: [2]

    sol = Solution(head = ListNode().populateFromArr(head))
    sol.main()