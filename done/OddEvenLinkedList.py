from timeit import default_timer as timer
from typing import List, Optional
from pack.ListNode import ListNode

class Solution:
    def __init__(self, head: ListNode):
        self.head = head
        print("init")

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        
        odd.next = even_head

        return head

    def main(self):
        start = timer()
        self.oddEvenList(ListNode().populateFromArr(head)).traverse()
        # Function call
        print(f"{timer() - start:.20f}")
    
if __name__ == "__main__":
    # head = [1,2,3,4,5] # Output: [1,3,5,2,4]
    head = [2,1,3,5,6,4,7] # Output: [2,3,6,7,1,5,4]

    sol = Solution(ListNode().populateFromArr(head))
    sol.main()