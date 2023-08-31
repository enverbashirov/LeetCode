from timeit import default_timer as timer
from typing import List, Optional
from pack.ListNode import ListNode
from time import sleep

class Solution:
    def __init__(self, head):
        self.head = head
        self.t1 = ListNode()
        self.t2 = self.t1
        print("init")

    def last(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if node.next: self.t2 = self.last(node.next)
        self.t2.next = ListNode()
        self.t2.next.val = node.val
        self.t2 = self.t2.next
        return self.t2

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.t1 = None
        if head:
            self.t1 = ListNode()
            self.t2 = self.t1
            self.last(head)
            self.t1 = self.t1.next
        return self.t1

    def main(self):
        tail = self.reverseList(self.head)
        tail.traverse()
        return

if __name__ == "__main__":
    # head = [1,2,3,4,5]
    # head = [1,2]
    head = []

    head = ListNode().populateFromArr(head)
    head.traverse()
    # sleep(1)

    sol = Solution(head)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
