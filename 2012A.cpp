//등수 매기기
//자료형 주의!!
//너무 어렵게 생각했다. 문제 풀이 도중에 인원보다 큰 등수를 사용했는데
//인원 보다 큰 등수는 있을 수 없다. 왜냐하면 예상등수는 이미 주어지고 내가 실제 등수를 정함으로써 불만도를 최소화
//시켜야 되기 때문이다.
#include <bits/stdc++.h>
using namespace std;

int N, arr[500000];

bool DESC(int a, int b){
    return a > b;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);

    cin >> N;
    for(int i = 0; i < N; ++i){
        cin >> arr[i];
    }

    sort(arr,arr + N, DESC);

    long long result = 0;
    int real = N;
    for(int i = 0; i < N; ++i){
        result += abs(arr[i] - real);
        real--;
    }
    
    cout << result;

    return 0;
}