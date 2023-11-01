from timeit import default_timer as timer
from typing import List

# 2 (Dictionary + 2D-List)
class TimeMap:

    def __init__(self):
        self.structure = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.structure:
            self.structure[key] = []
        self.structure[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        temp = self.structure.get(key, [])

        low, high = 0, len(temp) - 1
        while low <= high:
            mid = (low + high) // 2

            if temp[mid][1] <= timestamp:
                ans = temp[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return ans

# 1 (2D-Dictionary)
# class TimeMap:
#     def __init__(self):
#         self.d = dict()

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.d: self.d[key] = dict(); self.d[key] = {timestamp: value}
#         elif timestamp not in self.d[key]: self.d[key][timestamp] = value
#         elif self.d[key][timestamp] != value: self.d[key][timestamp] = value

#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.d: return ""
#         if self.d[key] == dict(): return ""
#         if timestamp not in self.d[key]: 
#             if [*self.d[key]][0] > timestamp: return ""
#             return self.d[key][max([k for k in [*self.d[key]] if k <= timestamp])]
#         return self.d[key][timestamp]

class Solution:
    def __init__(self, acts, vals):
        self.acts = acts
        self.vals = vals
        self.tm = TimeMap() #To be assigned as TimeMap()

    def main(self):
        for i, a in enumerate(self.acts):
            if a == 'TimeMap':
                self.tm = TimeMap()
            elif a == 'set':
                self.tm.set(vals[i][0], vals[i][1], vals[i][2])
            elif a == 'get':
                print(self.tm.get(vals[i][0], vals[i][1]))
            # print(i, a, self.tm.d)

        return self.tm

if __name__ == "__main__":
    # acts = ["TimeMap", "set", "get", "get", "set", "get", "get"]; 
    # vals = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

    acts = ["TimeMap","set","set","get","get","get","get","get"]
    vals = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

    sol = Solution(acts, vals)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
