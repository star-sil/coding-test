
//피보나치 수 2
//시간 초과..... fibo 함수 사용시...
//오버플로우 발생 변수 선언 int형으로 할시, 또는 long데이터 형을 %d로 출력하면 형변환이 되는데
//거기서 자동적으로 데이터가 소실됨
//int 형: -2,147,483,648 ~ 2,147,483,647 대충 20억 넘어가면 오버플로우 따라서 이때는 long을 사용하자
#include <stdio.h>
int fibo(int n)
{
    if(n == 1){
        return 1;
    }
    else if(n == 0){
        return 0;
    }
    return fibo(n-1) + fibo(n-2); 
}


int main(){
    int n;
    scanf("%d",&n);
    long num1 = 1;
    long num2 = 1;
    long num3 = 1;
    if(n == 1)
    {
        printf("%d",1);
        return 1;
    }
    if(n == 0)
    {
        printf("%ld",0);
        return 1;
    }
    for(int i = 3; i <= n; i++){
        num3 = num2 + num1;
        num1 = num2;
        num2 = num3;
    }
    printf("%ld",num3);
}