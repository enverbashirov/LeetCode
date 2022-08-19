
// import pack.*;
import java.util.*;
import java.util.stream.Collectors;

/*
cababababac
a={1,8} b={2,5} c={0,9}
"eccbbbbdec"

*/

class PartitionLabels {
  public static void main(String args[]){
    String s = "caedbdedda"; // ans = [9,7,8]
    
    PartitionLabels object = new PartitionLabels();
    List<Integer> ans = object.partitionLabels(s);

    System.out.println(ans);
  }  

  public static List<Integer> partitionLabels(String s) {
    char[] chars = s.toCharArray();
    Map<Character, int[]> letters = new LinkedHashMap();
    List<Integer> ans = new ArrayList<Integer>();

    for (int i = 0; i < chars.length; i++) {
      int first_index = i;
      if(letters.containsKey(chars[i]))
        first_index = letters.get(chars[i])[0];

      letters.put(chars[i], new int[] {first_index, i});
    }

    System.out.println();
    for (Map.Entry<Character, int[]> set : letters.entrySet()) {
      System.out.print(set.getKey() + "={" + set.getValue()[0] + "," + set.getValue()[1] + "} ");
    }

    int indices[] = new int[] {0, 0};
    for (Map.Entry<Character, int[]> set : letters.entrySet()) {
      if ( indices[1] < set.getValue()[0]) {
        ans.add(indices[1] - indices[0] + 1);
        indices = new int[] {set.getValue()[0], set.getValue()[1]};
      } else {
        if ( indices[1] < set.getValue()[1]) {
          indices[1] = set.getValue()[1];
        }  
      }
    }

    ans.add(indices[1] - indices[0] + 1);
    return ans;
  }
}