
class AddTwoNumbers {
  public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode lhead = new ListNode();
    ListNode ltail = lhead, l1tail = l1, l2tail = l2;
    boolean carry = false,
            l1done = (l1tail == null) ? true : false,
            l2done = (l2tail == null) ? true : false;

    while ( !l1done || !l2done ) {
      int res = 0;

      if( !l1done ) res += l1tail.val;
      if( !l2done) res += l2tail.val;

      l1done = (l1tail.next == null) ? true : false;
      l2done = (l2tail.next == null) ? true : false;

      if( carry) {
        res++; 
        carry = !carry;
      }

      if( res >= 10) {
        res -= 10; carry = true;
      }

      ltail.val = res;

      if (!l1done) l1tail = l1tail.next;
      if (!l2done) l2tail = l2tail.next;
      
      if (!l1done || !l2done) { 
        ltail.next = new ListNode(); 
        ltail = ltail.next;
      } else if ( carry ) {
        ltail.next = new ListNode();
        ltail.next.val = 1;
      }
    }
    return lhead;
  }
  
  public static void main(String args[]){ 

    // System.out.println();
    int[] n1 = {2,4,3};
    int[] n2 = {5,6,4};
    // System.out.println(n1.length);

    ListNode l1 = new ListNode().populateList(n1);
    System.out.print("Input1: "); l1.printList();
    ListNode l2 = new ListNode().populateList(n2);
    System.out.print("Input2: "); l2.printList();

    ListNode l = new AddTwoNumbers().addTwoNumbers(l1, l2);
    System.out.print("Output: "); l.printList();
  }
}

class ListNode {
  int val;
  ListNode next;
  ListNode() {}
  ListNode(int val) { this.val = val; }
  ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  void printList() {
    ListNode ltail = this;
    while( ltail != null) {
      System.out.print(ltail.val);
      ltail = ltail.next;
    }
    System.out.println();
  }
  ListNode populateList(int[] n){
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
  int[] getAsArray(ListNode l) {
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