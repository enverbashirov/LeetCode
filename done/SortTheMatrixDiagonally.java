// import pack.*;
import java.util.*;
import java.util.Arrays;

class SortTheMatrixDiagonally {
  public static void main(String args[]){
    // int[][] mat = new int[][] {{3,3,1,1},{2,2,1,2},{1,1,1,2}};
    int[][] mat = new int[][] {{11,25,66,1,69,7},{23,55,17,45,15,52},{75,31,36,44,58,8},{22,27,33,25,68,4},{84,28,14,11,5,50}};
    /*
    11 25 66 1  69 7
    23 55 17 45 15 52
    75 31 36 44 58 8
    22 27 33 25 68 4
    84 28 14 11 5 50

    5  17 4  1  52 7 
    11 11 25 45 8  69
    14 23 25 44 58 15
    22 27 31 36 50 66
    84 28 75 33 55 68
    */
    
    SortTheMatrixDiagonally obj = new SortTheMatrixDiagonally();
    
    obj.prettyPrint(obj.diagonalSort(mat));
  }  

  public int[][] diagonalSort(int[][] mat) {
    // Row-first
    for ( int i = 0; i < mat[0].length; i++) {
      // diag_length : min(n, m-i)
      int diag_length = mat.length < mat[0].length - i ? mat.length : mat[0].length - i;

      int [] diagonal = new int [diag_length];

      for ( int j = i; j < i + diag_length; j++) {
        diagonal[j-i] = mat[j-i][j];
      }

      Arrays.sort( diagonal);
      
      for ( int j = i; j < i + diag_length; j++) {        
        mat[j-i][j] = diagonal[j-i];
      }
    }
    
    // Column-first
    for ( int i = 1; i < mat.length; i++) {
      // diag_length : min(n-i, m)
      int diag_length = mat.length - i < mat[0].length ? mat.length - i : mat[0].length;
      int [] diagonal = new int [diag_length];

      for ( int j = i; j < i + diag_length; j++) {
        diagonal[j-i] = mat[j][j-i];
      }

      Arrays.sort( diagonal);
      
      for ( int j = i; j < i + diag_length; j++) {     
        mat[j][j-i] = diagonal[j-i];
      }
    }
    
    return mat;
  } 

  public void prettyPrint(int[][] mat) {
    for (int[] x : mat)
    {
      for (int y : x)
      {
        System.out.print(y + " ");
      }
      System.out.println();
    }
  }
}