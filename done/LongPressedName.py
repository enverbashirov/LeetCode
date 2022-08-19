from timeit import default_timer as timer
from typing import List
from itertools import groupby

class LongPressedName:
    def __init__(self, name, typed):
        self.name = name
        self.typed = typed
        print("init")

    def isLongPressedName(self, name: str, typed: str) -> bool:
        typedlist = [''.join(g) for _, g in groupby(typed)]
        namelist = [''.join(g) for _, g in groupby(name)]
        print(namelist)
        print(typedlist)

        if len(typedlist) != len(namelist): return False

        for i, c in enumerate(namelist):
            if c not in typedlist[i]: return False
        return True

    def main(self):
        print(self.isLongPressedName(self.name, self.typed))

if __name__ == "__main__":
    # name = "alex"
    # typed = "aaleex"
    name = "saeed"
    typed = "ssaaedd"

    sol = LongPressedName(name, typed)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
