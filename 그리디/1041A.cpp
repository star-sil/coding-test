/**
주사위

로직은 구했지만 문제이해를 정확히 하지 못함
주사위는 모두 같은것이고 그리고 한 면의 숫자도 정해지기 때문에 임의로 숫자를 변경할 수 없다.
한면이 보이게 되면 마주보는 면은 안보이게 됨 -> 둘중 가장 작을 것을 선택
**/

#include <iostream>
#include <algorithm>

using namespace std;

int N, dice[6], sum[4], total, big;
int n1,n2,n3;
long long answer;

int main(){
    
    cin >> N;

    for(int i = 0; i < 6; ++i){
        cin >> dice[i];
        total += dice[i];
        if(big < dice[i]) big = dice[i];
    }

    sum[0] = min(dice[0],dice[5]);
    sum[1] = min(dice[2],dice[3]);
    sum[2] = min(dice[1],dice[4]);
    sum[3] = total - big;

    sort(sum,sum + 3);

    if(N == 1){
        cout << sum[3] * 4;
    }
    else{
        answer += sum[0] * (long long)(N - 2)*(5 * N - 6);
        answer += (sum[0]+sum[1]) * (8 * N - 12);
        answer += (sum[0]+sum[1]+sum[2]) * 4;
        cout << answer;
    }
}