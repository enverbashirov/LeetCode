import pack.TreeNode;

class InvertBinaryTree {
  public TreeNode invertTree(TreeNode root) {
    if ( root == null) return null;
    return parseSubTree(root);
  }

  TreeNode parseSubTree(TreeNode root) {
    TreeNode output = new TreeNode(root.val);
    if( root.right != null) output.left = parseSubTree(root.right);
    if( root.left != null) output.right = parseSubTree(root.left);
    return output;
  }

  public static void main(String args[]){ 
    Object[] input = {4, 2, 7, 1, 3, 6, 9};
    TreeNode t = new TreeNode().populateTree(input);
    t.printTree();

    new InvertBinaryTree().invertTree(t).printTree();
  }  
}