/**
크게 만들기

숫자의 위치는 변경되면 안된다.

다음 숫자가 전에 숫자까지 작을때까지 앞에 숫자를 제거한다.
**/
#include <iostream>
#include <queue>
#include <vector>

using namespace std;


int N, K;
char str[500000];
vector<char> result;

int main(){
    cin >> N >> K;
    for(int i = 0; i < N; ++i){
        char tmp; cin >> tmp;
        str[i] = tmp;
    }

    for(int i = 0; i < N; ++i){
        while(!result.empty()&& result.back() < str[i] && K){
            result.pop_back();
            K--;
        }
        result.push_back(str[i]);
    }

    //빼야될 수가 남아있을땐 뒤에서 부터 뺀다.
    for(int i = 0; i < result.size() - K; ++i){
        cout << result[i];
    }
   
}