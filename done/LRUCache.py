from timeit import default_timer as timer

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict = {}
        self.queue: list = []
        print("init")

    def adjust_queue(self, key: int) -> None:
        if key in self.queue:
            self.queue.remove(key)
        elif self.capacity == len(self.queue):
            self.queue.pop(-1)
        self.queue.append(key)

    def adjust_cache(self, key: int) -> None:
        if key in self.cache.keys():
            self.cache.pop(key)

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.adjust_queue(key)
        
        if key in self.cache.keys(): 
            return self.cache[key]
        else: 
            return -1
        
    def put(self, key: int, value: int) -> None:
        self.adjust_queue(key)
        self.adjust_cache(key)

        if len(self.cache.keys()) == self.capacity:
            self.cache.pop(next(iter(self.cache)))

        self.cache[key] = value
    
if __name__ == "__main__":
    action = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    params = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    obj = None

    for i in range(len(action)):
        print(f"Action: {action[i]}, Params: {params[i]}", end=" => ")
        if action[i] == "LRUCache":
            obj = LRUCache(params[i][0])
            print(obj.capacity, end=" => ")
        elif action[i] == "put":
            obj.put(params[i][0], params[i][1])
        elif action[i] == "get":
            print(obj.get(params[i][0]), end=" => ")
        print(obj.cache)

