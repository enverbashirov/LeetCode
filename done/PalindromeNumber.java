class PalindromeNumber {
  public boolean isPalindrome(int x) {
    if(x < 0) return false;    

    int i = x;
    int reversed = 0;
    while(i != 0) {
      reversed = reversed * 10 + (i % 10);
      i /= 10;
    }
    
    if(x - reversed == 0) return true;
    return false;
  }

  public boolean isPalindrome2(int x) {
    if(x < 0) return false;    

    String str = Integer.toString(x);

    for(int i = 0; i < str.length() / 2; i++) {
      if(str.charAt(i) != str.charAt((str.length()-1)-i))
        return false;
    }
    return true;
  }
  
  public static void main(String args[]){  
    int x = 221;
    System.out.println(new PalindromeNumber().isPalindrome(x));
  }  
}