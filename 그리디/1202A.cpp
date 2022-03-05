/**
보석 도둑

max를 이용하지 말고 우선순위 큐를 사용해서 풀면 된다.
또한 이중루프라고 해서 반드시 시간초과하는 것이 아니다.
밑에 같은 경우는 최악에 경우라도 첫번째 루프에 대해 두번째 루프가 K번씩 반복되지 않는다.
왜냐하면 두번째 깊이에 있는 루프는 모든 경우에 대해 총 K번만 돌면된다. O(N+K)
**/

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
typedef pair<int,int> ii;

vector<ii> vii;
int N, K, Bags[3000000];
priority_queue<int> pq;

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> N >> K;
    for(int i = 0; i <N; ++i){
        int weight, price;
        cin >> weight >> price;
        vii.push_back(ii(weight,price));
    }

    for(int i = 0; i < K; ++i){
        cin >> Bags[i];
    }

    sort(Bags, Bags + K); sort(vii.begin(),vii.end());

    long long result = 0; int j =0;
    for(int i = 0; i < K; ++i){
        int maxWeight = Bags[i];
        for(; j < N; ++j){
            if(maxWeight < vii[j].first) break;
            else pq.push(vii[j].second);
        }
        if(!pq.empty()){
            result += pq.top(); pq.pop();
        }
    }
    cout << result;
}