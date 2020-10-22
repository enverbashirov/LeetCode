public class LongestCommonPrefix {
  public String longestCommonPrefix(String[] strs) {
    if( strs.length == 0) return "";
    if( strs.length == 1) return strs[0];

    String output = strs[0];
    int index = 0;

    for( int i = 1; i < strs.length; i++) {
      if( strs[i].length() < output.length()) {
        output = strs[i];
        index = i;
      } 
    }
    // System.out.println("Shortest: " + output + " Length: " + output.length());

    for( int i = 0; i < strs.length && output.length() != 0; i++) {
      if ( index == i) continue;
      for ( int j = 1; j <= output.length() && output.length() != 0; j++) {
        // System.out.println(output.substring(0, j) + " " + strs[i].substring(0, j));
        if ( !output.substring(0, j).equals(strs[i].substring(0, j))) {
          output = output.substring(0, j-1);
          // System.out.print("test");
        }
      }
    }

    return output;
  }  
  public static void main(String args[]){ 
    String[] input = {"flower","flow","flight"};
    System.out.println("Output: " + new LongestCommonPrefix().longestCommonPrefix(input));
  }  
}
