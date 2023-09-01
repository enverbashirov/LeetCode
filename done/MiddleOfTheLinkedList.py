from timeit import default_timer as timer
from typing import List, Optional
from pack.ListNode import ListNode

class Solution:
    def __init__(self, head):
        self.head = head
        print("init")

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        go = True

        while(head.next):
            head = head.next
            if go: ans = ans.next
            go = not go
        return ans
    
    def main(self):
        print(self.middleNode(self.head).val)
        return

if __name__ == "__main__":
    head = [1,2,3,4,5] # 3
    # head = [1,2,3,4,5,6] # 4

    head = ListNode().populateFromArr(head)
    sol = Solution(head)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
