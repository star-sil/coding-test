import java.util.*;

class Solution {
    public int solution(int[] citations) {
        
        Arrays.sort(citations);
        
        int answer = citations[0];
        
        for(int i = 0; i < citations.length; i++){
            int h = citations.length - i; // 나머지 논문 개수
            if(citations[i] >= h) {
                answer = h;
                break;
            }
        }
        
        return answer;
    }
}