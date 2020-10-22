import java.util.ArrayList;

class LongestSubstringWithoutRepeatingCharacters {

  public int lengthOfLongestSubstring(String s) {
    int iTotal = 0;

    for( int i = 0; i + 1 < s.length(); i++) {
      ArrayList<Character> chars = new ArrayList<Character>();
      chars.add(s.charAt(i));
      
      for( int j = i + 1; j < s.length(); j++) {
        if( chars.contains(s.charAt(j)) ) {
          if( (j - i) > iTotal || iTotal == s.length()) {
            iTotal = j - i;
          }
          break;
        } 
        else if ( j + 1 == s.length() && ( (j + 1) - i > iTotal)) {
          iTotal = (j + 1) - i;
        }
        chars.add(s.charAt(j));
      }
    }
    if ( iTotal == 0) iTotal = s.length();
    return iTotal;
  }

  public static void main(String args[]){ 
    String input = "asdffffassd";
    System.out.println("Result: " + new LongestSubstringWithoutRepeatingCharacters().lengthOfLongestSubstring(input));
  }  
}