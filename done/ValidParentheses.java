import java.util.HashMap;

class ValidParentheses {
  public boolean isValid(String s) {
    char[] c = s.toCharArray();
    HashMap<Integer, Character> map = new HashMap<Integer, Character>();
    int last = 0;

    for ( int i = 0; i < c.length; i++) {
      // System.out.println(map + Integer.toString(last));
      if ( c[i] == '(' || c[i] == '[' || c[i] == '{' ) { last++; map.put(last, c[i]);}
      else if ( last == 0) return false;
      else switch( map.remove(last--)){
        case '(': if ( c[i] != ')') return false; break;
        case '[': if ( c[i] != ']') return false; break;
        case '{': if ( c[i] != '}') return false; break;
        default: return false;
      }
    }
    if ( last != 0) return false; return true;
  }
  public static void main(String args[]){ 
    // String input = "()";
    String input = "";
    System.out.println(new ValidParentheses().isValid(input));
  }  
}