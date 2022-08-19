from timeit import default_timer as timer
from typing import List

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min != []:
            self.min.append(min(val, self.min[-1]))
        else:
            self.min.append(val)
        
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.min.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        return self.min[-1] if self.min else None

    def main(self):
        # Your MinStack object will be instantiated and called as such:
        val1 = ["MinStack","push","push","push","push","pop","getMin","pop","getMin","pop","getMin"]
        val2 = [[],[512],[-1024],[-1024],[512],[],[],[],[],[],[]]

        obj = MinStack()
        for i, val in enumerate(val1):
            print(len(obj.stack), len(obj.min))
            if val == "push":
                print(obj.push(val2[i]))
                # print(val2[i], val)
            if val == "pop":
                print(obj.pop())
            if val == "top":
                print(obj.top())
            if val == "getMin":
                print(obj.getMin())

if __name__ == "__main__":
    sol = MinStack()
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
