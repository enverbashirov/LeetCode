from timeit import default_timer as timer
from typing import List, Optional
from pack.Graph import Graph as Node
from collections import deque

class Solution:
    def __init__(self, node):
        self.node = node
        print("init")

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]

    def main(self):
        self.cloneGraph(self.node).display()
        return

if __name__ == "__main__":
    adjList = [[2,4],[1,3],[2,4],[1,3]] #Output: [[2,4],[1,3],[2,4],[1,3]]
    # adjList = [[]] #Output: [[]]
    # adjList = [] #Output: []

    node = Node().populate(adjList)
    node.display()

    sol = Solution(node)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
