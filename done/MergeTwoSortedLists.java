import pack.ListNode;

class MergeTwoSortedLists {
  public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    if (l1 == null && l2 == null) return null;
    
    ListNode output = new ListNode();
    ListNode templ1 = l1, templ2 = l2, tail = output, temptail = output;

    while(templ1 != null && templ2 != null) {
      if ( templ1.val <= templ2.val) {
        tail.val = templ1.val;
        templ1 = templ1.next;
      } else {
        tail.val = templ2.val;
        templ2 = templ2.next;
      }
      temptail = tail;
      tail.next = new ListNode();
      tail = tail.next;
    }
    while(templ1 != null) {
      tail.val = templ1.val;
      templ1 = templ1.next;
      temptail = tail;
      tail.next = new ListNode();
      tail = tail.next;
    }
    while(templ2 != null) {
      tail.val = templ2.val;
      templ2 = templ2.next;
      temptail = tail;
      tail.next = new ListNode();
      tail = tail.next;
    }
    temptail.next = null;
    return output;
  }
  public static void main(String args[]){ 
    int[] n1 = {-9,3}, n2 = {5,7};
    ListNode l1 = new ListNode().populateList(n1);
    System.out.print("Input1: "); l1.printList();
    ListNode l2 = new ListNode().populateList(n2);
    System.out.print("Input2: "); l2.printList();

    ListNode l = new MergeTwoSortedLists().mergeTwoLists(l1, l2);
    System.out.print("Output: "); l.printList();
  }  
}