/**
평범한 배낭

배낭문제라는 주제가 따로 있었다.
짐을 쪼갤 수 있는경우 -> 그리디
짐을 쪼갤 수 없는 경우 -> dp

이 문제는 쪼갤 수 없으므로 dp로 풀어야한다. dp[i][j]는  i번째 물건중 j의 무게 제한일때 가장 큰 가치를 의미한다.
재귀적으로 문제를 접근하면된다.
**/

#include <iostream>

using namespace std;

int N, K, w[101],v[101], dp[101][100001];

int main(){
    cin >> N >> K;

    for(int i = 1; i <= N; ++i){
        cin >> w[i] >> v[i];
    }

    for(int i = 1; i <= N; ++i){
        for(int j = 1; j <= K; ++j){
            if(w[i] <= j){
                dp[i][j] = max(dp[i-1][j],dp[i-1][j - w[i]] + v[i]);
            }
            else{
                dp[i][j] = dp[i-1][j];
            }
        }
    }

    cout << dp[N][K];
}