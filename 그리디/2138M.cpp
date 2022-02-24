/**
전구와 스위치
왼쪽을 우선순위로 변경 왼쪽은 다음부터는 변경불가

왼쪽이 변경해야함 -> 무조건 변경
왼쪽이 변경안해야함 -> 무조건 넘어감
왼쪽 없는경우 -> 자신 판별
입력이 붙어있는 경우는 문자열로 입력받음
전역변수로 초기화 시킬 수 있다.(result)
**/
#include <iostream>

using namespace std;

#define MAX 987654321;

string first, second;
int N,result = -1;

void lightOn(int k){
    string tmp = first;
    int cnt = 0;
    if(k == 0){
        tmp[0] = (tmp[0] == '1') ? '0' : '1';
        tmp[1] = (tmp[1] == '1') ? '0' : '1';
        cnt++;
    }
    for(int i = 1; i < N; ++i){
        if(tmp[i-1] != second[i-1]){ 
            tmp[i-1] = (tmp[i-1] == '1') ? '0' : '1';
            tmp[i] = (tmp[i] == '1') ? '0' : '1';
            tmp[i+1] = (tmp[i+1] == '1') ? '0' : '1';
            cnt++;
        }
    }

    if(tmp == second){
        if(result == -1) result = cnt;
        else result = min(cnt,result);
    }
}

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> N >> first >> second;

    lightOn(0); lightOn(1);

    cout << result;
    return 0;
}