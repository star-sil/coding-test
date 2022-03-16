/**
센서

문제이해가 어려웠음 문제가 요구하는 것을 정확히 파악하는 것이 중요!!
수신 가능 영역의 길이의 합을 최소화 해야됨 -> 단순히 더해서 또는 최적의 거리를 찾는것이 아닌 가장 큰 센서들간의 거리를 집중국의 범위에 속하지 않도록
하는 것이 중요하다.
**/
#include <iostream>
#include <algorithm>

using namespace std;

int N, K, sens[10000], dist[9999], result;

int main(){
    cin >> N >> K;
    for(int i = 0; i < N; ++i){
        cin >> sens[i];
    }

    sort(sens,sens + N);

    for(int i = 1; i < N; ++i){
        dist[i] = sens[i] - sens[i-1];
    }

    sort(dist,dist + N,greater<int>());

    for(int i = K - 1; i < N -1; ++i){
        result += dist[i];
    }
    cout << result;
    
}