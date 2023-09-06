
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        x = None
        if len(self.queue) > 0:
            x = self.queue[0]
            self.queue = self.queue[1:]
        return x

    def peek(self) -> int:
        if len(self.queue) > 0: return self.queue[0]
        return None

    def empty(self) -> bool:
        return self.queue == []
    
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