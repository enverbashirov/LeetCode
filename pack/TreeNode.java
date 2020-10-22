package pack;

public class TreeNode {
  public int val;
  public TreeNode left;
  public TreeNode right;
  public TreeNode() {}
  public TreeNode(int val) { this.val = val; }
  public TreeNode(int val, TreeNode left, TreeNode right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
  
  public void printTree() {
    if( val != 0) printTree(this);
    System.out.println();
  }
  public void printTree( TreeNode root) {
    System.out.print(root.val);
    if( root.left != null) printTree( root.left);
    if( root.right != null) printTree( root.right);
  }

  public TreeNode populateTree( Object[] input) {
    populateTree(this, 0, input);
    return this;
  }
  public void populateTree( TreeNode root, int index, Object[] input ) {
    if( input.length > index && input[index] != null) root.val = (int) input[index];
    if( input.length > ((index * 2) + 1) && input[((index * 2) + 1)] != null) { 
      root.left = new TreeNode(); 
      populateTree(root.left, ((index * 2) + 1), input); 
    }
    if( input.length > ((index * 2) + 2) && input[((index * 2) + 2)] != null) { 
      root.right = new TreeNode(); 
      populateTree(root.right, ((index * 2) + 2), input); 
    }
  }
}