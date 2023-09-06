
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
    