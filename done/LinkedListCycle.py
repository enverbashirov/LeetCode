from timeit import default_timer as timer
from typing import List, Optional
from pack.ListNode import ListNode

class Solution:
    def __init__(self, head: ListNode()):
        self.head = head
        print("init")

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False
    
    def main(self):
        self.hasCycle(self.root)
        return

if __name__ == "__main__":
    # head = ...
    # head = ListNode(head)

    # ListNode implementation missing 
    sol = Solution(head = None)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
