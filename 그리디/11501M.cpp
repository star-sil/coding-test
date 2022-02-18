//주식
//거꾸로 for문 돌릴때 범위 체크....(N이 아니라 N-1)
//테스트 케이스 마다 결과를 출력해야되는 것은 바로바로 결과를 출력하라는 의미
//한번에 출력하면 안된다.
#include<iostream>
#include<vector>

using namespace std;

int N, T, stocks[1000000];
vector<long long> result;

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> T;
    for(int i = 0; i < T; ++i){
        cin >> N;
        for(int j =0; j < N; ++j)
            cin >> stocks[j];
        
        int max = 0; long long addStock = 0;
        for(int j = N-1; j >= 0; --j){
            if(stocks[j] >= max) max = stocks[j];
            else addStock += max - stocks[j];
        }
        cout << addStock << "\n";
    }

    return 0;
    
}