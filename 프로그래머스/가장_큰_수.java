import java.util.*;


class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        List<String> strNumbers = new ArrayList<>();
        
        
        
        for(int i = 0; i < numbers.length; i++){
            strNumbers.add(numbers[i] + "");
        }
        
        Collections.sort(strNumbers, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                return (b+a).compareTo(a+b);
            }
        });
        
        for(String number : strNumbers){
            answer += number;
        }
        
        if (answer.charAt(0) == '0') return "0";
        
        return answer;
    }
}