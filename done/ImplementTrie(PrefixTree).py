from timeit import default_timer as timer
from time import sleep
from typing import List
# from pack import Trie

class Trie:

    def __init__(self):
        self.root={}
        
    def insert(self, word: str) -> None:

        cur=self.root

        for letter in word:
            if letter not in cur:
                cur[letter]={}
            cur=cur[letter]

        cur['*']=''

    def search(self, word: str) -> bool:

        cur=self.root
        for letter in word:
            if letter not in cur:
                return False
            cur=cur[letter]

        return '*' in cur
        
    def startsWith(self, prefix: str) -> bool:

        cur=self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur=cur[letter]

        return True
    
if __name__ == "__main__":
    acts = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    vals = [[], ["apple"], ["apple"], ["app"], ["startsWith"], ["insert"], ["search"]]

    # Your Trie  object will be instantiated and called as such:
    start = timer()
    for i, a in enumerate(acts):
        if a == "Trie":
            obj = Trie()
        if a == "insert":
            ans = obj.insert(vals[i][0])
            print("insert", vals[i][0], ans)

        if a == "search":
            ans = obj.search(vals[i][0])
            print("search", vals[i][0], ans)

        if a == "startsWith":
            ans = obj.startsWith(vals[i][0])
            print("startsWith", vals[i][0], ans)

    print(f"{timer() - start:.20f}")
