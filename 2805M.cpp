//나무 자르기(문제 유형: 파라메타 서치)
// 처음 틀렸을때는 result의 데이터 형을 int로 두었다.
// 하지만 여기서는 result의 최대치가 int형의 표현 범위를 넘기기때문에 오버플로우를 생각해 long으로 변경해야한다.
#include <stdio.h>
int main()
{
    int N, M;
    int arr[1000000] = {0,};
    scanf("%d %d",&N, &M);

    for(int i = 0; i < N; i++)
    {
        scanf("%d",&arr[i]);
    }
    int head = 0;
    int tail = 1000000000;
    int mid = 0;
    while(head <= tail)
    {
        mid = (head + tail) / 2;
        long result = 0;
        for(int i = 0; i < N; i++){
            if(arr[i] > mid)
            {
                result += (arr[i] - mid);
            }
        }
        if(result >= M){
            head = mid + 1;
        }
        else{
            tail = mid - 1;
        }
    }
    printf("%d",tail);
}