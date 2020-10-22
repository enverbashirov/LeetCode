class RomanToInteger {
  public int romanToInt(String s) {
    String romans = "IVXLCDM";
    int[] value = {1, 5, 10, 50, 100, 500, 1000};
    int output = 0;

    for(int i = s.length() - 1; i >= 0; i--) {
      if ((i - 1) >= 0 &&
          romans.indexOf(s.charAt(i)) - romans.indexOf(s.charAt(i - 1)) <= 2 &&
          romans.indexOf(s.charAt(i)) - romans.indexOf(s.charAt(i - 1)) > 0) {
        output += value[romans.indexOf(s.charAt(i))] - value[romans.indexOf(s.charAt(i - 1))];
        i--;
      } else output += value[romans.indexOf(s.charAt(i))];
      // System.out.println(i + " " + s.charAt(i) + " " + romans.indexOf(s.charAt(i)) + " " + output);
    }
    return output;
  }

  public static void main(String args[]){ 
    String input = "MCMXCIV";
    System.out.println(new RomanToInteger().romanToInt(input));
  }  
}