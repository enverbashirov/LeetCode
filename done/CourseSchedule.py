from timeit import default_timer as timer
from typing import List
from collections import defaultdict

class Solution:
    def __init__(self, numCourses, prerequisites):
        self.numCourses = numCourses
        self.prerequisites = prerequisites
        print("init")

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre = defaultdict(list)

        for course, p in prerequisites:
            pre[course].append(p)
        
        taken = set()

        def dfs(course):
            if not pre[course]:
                return True
            
            if course in taken:
                return False
            
            taken.add(course)

            for p in pre[course]:
                if not dfs(p): return False
            
            pre[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        
    def main(self):
        print(self.canFinish(self.numCourses, self.prerequisites))
        return

if __name__ == "__main__":
    numCourses = 2; prerequisites = [[1,0]] #Output: true
    # numCourses = 2; prerequisites = [[1,0],[0,1]] #Output: false

    sol = Solution(numCourses, prerequisites)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
