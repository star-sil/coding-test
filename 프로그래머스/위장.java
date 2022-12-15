import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String,List<String>> map = new HashMap<>();
        
        for(String[] cloth : clothes){
            if( map.containsKey(cloth[1]))
                map.get(cloth[1]).add(cloth[0]);
            else {
                List<String> wears = new ArrayList<>();
                wears.add(cloth[0]);
                map.put(cloth[1],wears);
            }
        }
        
        
        Set<String> clothTypes = map.keySet();
        
        for(String type : clothTypes) {
            answer *= (map.get(type).size()+1);
        }
        answer -= 1;
        return answer;
    }
}