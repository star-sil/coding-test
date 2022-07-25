/*
 * 나머지 연산
 */
import java.util.Scanner;

public class A4375{
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int n = sc.nextInt();
            int num = 0;
            for(int i =1;;i++){
                num = num * 10 + 1;
                num %= n;
                if(num == 0){
                    System.out.println(i);
                    break;
                }
            }
        }
    }
}