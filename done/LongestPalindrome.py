from timeit import default_timer as timer
from typing import List

class Solution:
    def __init__(self, s):
        self.s = s
        print("init")

    def longestPalindrome(self, s: str) -> int:
        s = ''.join(sorted(s))
        ans, odd = 0, False
        while s:
            c = s[0]
            n = s.count(c)
            ans += n - (n % 2)
            if ~odd and n % 2 == 1: odd = ~odd
            s = s.replace(c, '')
        if odd: ans += 1
        return ans

    def main(self):
        print(self.longestPalindrome(self.s))
        return

if __name__ == "__main__":
    s = "abccccdd" # 7
    # s = "a" # 1
    s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth" # 983

    sol = Solution(s)
    start = timer()
    sol.main()
    print(f"{timer() - start:.20f}")
