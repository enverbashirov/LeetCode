import pack.TreeNode;

class PathSumIII {
  int paths = 0;
  int sum = 0;

  public int pathSum(TreeNode root, int sum) {
    if ( root == null) return 0;
    this.sum = sum;
    parseSubTree(root);
    return paths;
  }
  void parseSubTree(TreeNode root) {
    sumSubTree(root, 0);
    if( root.left != null) parseSubTree(root.left);
    if( root.right != null) parseSubTree(root.right);
  }
  void sumSubTree(TreeNode root, int curSum) {
    if( curSum + root.val == sum) paths++;
    if( root.left != null) sumSubTree(root.left, curSum + root.val);
    if( root.right != null) sumSubTree(root.right, curSum + root.val);;
  }

  public static void main(String args[]){ 
    Object[] input = new Object[]{1,-2,-3,1,3,-2,null,-1};
    TreeNode iTree = new TreeNode().populateTree( input);
    // iTree.printTree();
    
    System.out.println(new PathSumIII().pathSum(iTree, -1));
  }  
}