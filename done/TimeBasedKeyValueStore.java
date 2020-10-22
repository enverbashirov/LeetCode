
import java.util.HashMap;
import java.util.Map;

class TimeBasedKeyValueStore {
  /** Initialize your data structure here. */
  Map <String, Map<Integer, String> > timeMap;

  public TimeBasedKeyValueStore() {
    timeMap = new HashMap<String, Map<Integer, String>>();
  }

  public void set(String key, String value, int timestamp) {
    if(timeMap.get(key) == null)
      timeMap.put(key, new HashMap<Integer, String>());
    
    Map <Integer, String> tempMap = timeMap.get(key);
    tempMap.put(timestamp, value);
    timeMap.put(key, tempMap);
  }

  public String get(String key, int timestamp) {
    Map <Integer, String> tempMap = timeMap.get(key);
    for(int i = 0; timestamp - i >= 0; i++) {
      if (tempMap.get(timestamp - i) != null) 
        return tempMap.get(timestamp-i);
    }
    return "";
  }

  
  public static void main(String args[]){  
    String[] timestep = {"set","get","get","set","get","get"};
    KeyValue[] inputs = {
      new KeyValue("foo","bar",1),
      new KeyValue("foo",1),
      new KeyValue("foo",3),
      new KeyValue("foo","bar2",4),
      new KeyValue("foo",4),
      new KeyValue("foo",5)
    };

    TimeBasedKeyValueStore obj = new TimeBasedKeyValueStore();
    for ( int i = 0; i < timestep.length; i++){
      if ( timestep[i] == "set") obj.set(inputs[i].key, inputs[i].value, inputs[i].timestamp);
      else if ( timestep[i] == "get") System.out.println(obj.get(inputs[i].key, inputs[i].timestamp));
    }
  } 
}

class KeyValue{
  String key;
  String value;
  int timestamp;
  KeyValue(String key, String value, int timestamp) {
    this.key = key;
    this.value = value;
    this.timestamp = timestamp;
  }
  KeyValue(String key, int timestamp) {
    this.key = key;
    this.value = "";
    this.timestamp = timestamp;
  }
}