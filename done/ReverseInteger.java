class ReverseInteger {
  public int reverse(int x) {
    String str = Integer.toString(x);
    String reverse = "";

    for( int i = 0; i < str.length(); i++)
      reverse = str.charAt(i) + reverse;

    if(reverse.charAt(reverse.length()-1) == '-')
      reverse = '-' + reverse.substring(0,str.length()-1);

    try {
      return Integer.parseInt(reverse);
    } 
    catch (NumberFormatException e) {
      return 0;
    }
  }
  
  public static void main(String args[]){  
    int x = 2147483647;
    System.out.println(new ReverseInteger().reverse(x));
  }  
}