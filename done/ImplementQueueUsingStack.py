from timeit import default_timer as timer

class MyQueue:
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

if __name__ == "__main__":
    acts = ["MyQueue", "push", "push", "push", "peek", "pop", "empty"]
    vals = [[], [1], [2], [3], [], [], []]

    # Your MyQueue object will be instantiated and called as such:
    start = timer()
    for i, a in enumerate(acts):
        if a == "MyQueue":
            obj = MyQueue()
        print(obj.queue)
        if a == "push":
            obj.push(vals[i][0])
        if a == "pop":
            print(obj.pop())
        if a == "peek":
            print(obj.peek())
        if a == "empty":
            print(obj.empty())

    print(f"{timer() - start:.20f}")
