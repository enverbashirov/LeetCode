public class RepeatedSubstringPattern {
  public boolean repeatedSubstringPattern(String s) {
    for ( int i = 0; s.length() / (i+1) > 1; i++){
      if ( s.length() % (i+1) == 0 && 
          s.substring(0,(i+1)).repeat(s.length()/(i+1)).equals(s)) 
        return true;
    }

    return false;
  }
  public static void main(String args[]){ 
    String input = "abcabcabc";
    // System.out.println(new String(new char[2]).replace("\0", input.substring(0,1)));
    System.out.println(new RepeatedSubstringPattern().repeatedSubstringPattern(input));
  }  
}
