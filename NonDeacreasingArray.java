class NonDeacreasingArray {
  public boolean checkPossibility(int[] nums) {
    boolean change = false;
    for ( int i = 0; i+1 < nums.length; i++) {
      if ( nums[i] <= nums[i+1]) continue;
      if ( i > 0)
        if ( nums[i-1] + nums[i] > nums[i] + nums[i+1])
      if ( change) return false;
      change = !change;
    }

    return true;
  }
  public static void main(String args[]){ 
    int[] input = {1, 4, 3, 4};
    System.out.println(new NonDeacreasingArray().checkPossibility(input));
  }  
}