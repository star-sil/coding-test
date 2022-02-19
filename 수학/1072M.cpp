//게임
#include <stdio.h>
int main(){
    long X, Y;
    scanf("%ld %ld", &X, &Y);
    //long은 소숫점 표현 안됨 100 먼저 곱해줘야함
    long result = Y * 100 / X;
    if(result >= 99)
    {
        printf("%d" , -1);
        return -1;
    } 

    int tail = 1;
    int head = 1000000000;
    while(tail <= head)
    {
        int mid = (tail + head) / 2;
        int tmp = (mid + Y) * 100 / (mid + X);
        printf("%d %ld\n",tmp, result);
        if(tmp > result)
        {
            head = mid - 1;
        }
        else
        {
            tail = mid + 1;
        }
    }
    printf("%d",tail);
    return 1;
}