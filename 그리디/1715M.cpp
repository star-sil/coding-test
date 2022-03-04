/**
카드 정렬하기

큰수는 되도록 적게 더해저야됨
우선순위 큐 사용
벡터로 했을때와의 시간 복잡도가 많이 차이 나는가....
sort 평균 시간 복잡도 nlogn
**/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, result;
vector<int> Cards;

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    for(int i = 0; i < N; ++i){
        int tmp; cin >> tmp;
        Cards.push_back(tmp);
    }

    if(N == 1) cout << 0;
    else{
        while(Cards.size() > 1){
            //내림차순으로 정렬
            sort(Cards.begin(), Cards.end(), greater<int>());
            int v1 = Cards.back(); Cards.pop_back();
            int v2 = Cards.back(); Cards.pop_back();
            Cards.push_back(v1+v2); result += (v1 +v2);
        }
    }

    cout << result;
}