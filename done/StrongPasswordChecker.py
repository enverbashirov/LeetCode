from math import ceil

class Solution:
    def __init__(self):
        print("init")
    
    def strongPasswordChecker(self, s: str) -> int:
        upper = lower = digit = False
        for t in s:
            if upper and lower and digit: break
            elif not upper and t.isupper(): upper = True
            elif not lower and t.islower(): lower = True
            elif not digit and t.isdigit(): digit = True
        
        csym = 0 # no of missing symbol <lower, upper, digit>
        if not upper: csym += 1
        if not lower: csym += 1
        if not digit: csym += 1

        # crep: no of removals needed for repetations (for l > 20)
        # crep2: no of symbol changes needed for repetations (for 6 > l > 20)
        output = crep = crep2 = i = 0
        while i < len(s):
            if len(s) > i + 2 and s[i] == s[i+1]:
                temp = 0
                while len(s) > i + 2 and s[i] == s[i+2]:
                    temp += 1; i += 1
                crep += temp; crep2 += ceil(temp / 3)
                i += 1
            i += 1

        # if len(s) < 6:
        #     output = max((6 - len(s)), csym, ceil(crep / 3))
        # elif len(s) > 20:
        #     crep = max(0, crep - (len(s) - 20))
        #     output = (len(s) - 20) + max(min(ceil(crep / 3), crep2), csym)
        # else:
        #     output = max(csym, crep2)
        output = max((6 - len(s)), # l < 6
            csym, crep2, # 6 <= l <= 20 
            (len(s) - 20) + max(min(ceil(max(0, crep - (len(s) - 20)) / 3), crep2), csym)) # 20 < l

        return output
        
    def main(self):
        s = ["", "asdfgh", "asdfg", "asdf", "asd", "asdfG", "asdfG1", "QQQQQ", "aaa123", "aaa111", "aaaaaaaaaaaaaaaaaaaaa", "ABABABABABABABABABAB1", "1234567890123456Baaaaa"]
        t = [6, 2, 2, 2, 3, 1, 0, 2, 1, 2, 7, 2, 3]
        for i, _ in enumerate(s):
            r = self.strongPasswordChecker(s[i])
            if r != t[i]:
                print(r==t[i], "res", r, "cor", t[i], "len", len(s[i]), s[i])

if __name__ == "__main__":
    sol = Solution()
    sol.main()
 