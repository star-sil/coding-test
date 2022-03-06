/**
전화번호 목록

하나라도 속하는 문자열이 있으면 바로 NO를 출력
문자열 자르기 사용하면 됨
문자열을 정렬 시켰을때 현재 있는 숫자가 옆에 있는 숫자에 속하지 않으면
앞으로도 속하지 않는다.
**/

#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

string callNum[10000];
int T, N;

int main(){
    cin >> T;
    for(int t = 0; t < T; ++t){
        cin >> N; bool sign = false;
        for(int i = 0; i < N; ++i){
            cin >> callNum[i];
        }

        sort(callNum,callNum+N);
        
        for(int i = 0; i < N; ++i){
            if(callNum[i] == callNum[i+1].substr(0,callNum[i].size())){
                sign = true;
                cout << "NO" << "\n";
                break;
            }
        }

        if(!sign) cout << "YES" << "\n";
    }
}