public class Solution
{
    public char NextGreatestLetter(char[] letters, char target) {
        for(int i = 0; i < letters.Length; i++) {
            if (target < letters[i]) {
                return letters[i];
            }
        }
        return letters[0];
    }

    public static void Main(string[] args)
    {
        // char [] letters = new char [3]{'c','f','j'}; char target = 'a'; // Output: 'c'
        // char [] letters = new char [3]{'c','f','j'}; char target = 'c'; // Output: 'f'
        char [] letters = new char [4]{'x','x','y','y'}; char target = 'z'; // Output: 'x'        
        Solution sol = new Solution();
        System.Console.WriteLine(sol.NextGreatestLetter(letters, target));
    }
}