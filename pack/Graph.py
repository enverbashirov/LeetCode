from typing import List

class Graph:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def populate(self, arr):
        if arr != []:
            tmp = [Graph(i, None) for i in range(1, len(arr)+1)]
            for i, a in enumerate(arr):
                tmp[i].neighbors = [tmp[n-1] for n in a]
            
            self.val = tmp[0].val
            self.neighbors = tmp[0].neighbors

        return self

    def display(self, arr: List = []):
        if self.val > 0:
            print([self.val, [n.val for n in self.neighbors]])
            if self.val not in arr: arr.append(self.val)
            for n in self.neighbors:
                if n.val not in arr: n.display(arr)
        else:
            print([])

