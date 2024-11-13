using System;
public class Solution {    
public int CountBinarySubstrings(string s) {
    int prevGroupLength = 0;
    int currGroupLength = 1;
    int count = 0;

    for (int i = 1; i < s.Length; i++) {
        if (s[i] == s[i - 1]) {
            // Current character matches the previous, increment current group length
            currGroupLength++;
        } else {
            // When characters switch, add the minimum of prevGroupLength and currGroupLength to count
            count += Math.Min(prevGroupLength, currGroupLength);
            // Move current group length to previous, reset current to 1
            prevGroupLength = currGroupLength;
            currGroupLength = 1;
        }
    }
    // Final update for the last two groups
    count += Math.Min(prevGroupLength, currGroupLength);
    
    return count;
}

    public static void Main(string[] args)
    {
        string s = "00110011"; // Output: 6
        // string s = "10101"; // Output: 4 
 
        Solution sol = new Solution();
        System.Console.WriteLine(sol.CountBinarySubstrings(s));
    }
}