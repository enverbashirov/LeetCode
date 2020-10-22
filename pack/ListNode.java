package pack;

public class ListNode {
  public int val;
  public ListNode next;
  public ListNode() {}
  public ListNode(int val) { this.val = val; }
  public ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  
  public void printList() {
    ListNode ltail = this;
    while( ltail != null) {
      System.out.print(ltail.val);
      ltail = ltail.next;
    }
    System.out.println();
  }

  public ListNode populateList(int[] n){
    ListNode l = new ListNode(); 
    ListNode ltail = l;
    for( int i = 0; i < n.length; i++) {
      ltail.val = n[i];
      if( i+1 < n.length){
        ltail.next = new ListNode();
        ltail = ltail.next;
      }
    }
    return l;
  }
  
  public int[] getAsArray(ListNode l) {
    int count = 0;
    ListNode ltail = l;
    while(ltail != null){
      count++;
      ltail = ltail.next;
    }

    int[] n = new int[count];
    ltail = l;
    for(int i = 0; ltail != null; i++){
      n[i] = ltail.val;
      ltail = ltail.next;
    }

    return n;
  }
}