/**
크게 만들기

++접근 방법
숫자의 위치는 변경되면 안된다.
K개를 지울 수 있을때 K만큼 뒤에 큰수가 있으면 큰수 앞에는 다지우는 것이 좋다.
특정 문자열의 숫자는 앞에 자신보다 같거나 큰수가 있는 것이 좋다.

++풀이
다음 숫자가 전에 숫자까지 작을때까지 앞에 숫자를 제거한다. -> 그래도 K가 남을 경우는 중복되는 숫자가 많은 경우
-> 하지만 이 경우는 뒤에 있는 숫자가 앞에있는 숫자보다 작거나 크다는 것을 보장 -> 뒤에 부터 남은 K개를 제거
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