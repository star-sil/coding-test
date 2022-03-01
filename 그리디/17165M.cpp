/**
볼 모으기

그냥 구현문제
빨간색을 왼쪽으로 옮기는경우
빨간색을 오른쪽으로 옮기는경우
파란색을 왼쪽으로 옮기는경우
파란색을 오른쪽으로 옮기는경우
**/

#include <iostream>

using namespace std;

int N, result, cnt;
string Balls;
bool sign;

int main(){
    cin >> N; cin >> Balls;

    //빨간색을 왼쪽으로 옮기는 경우
    for(int i = N-1; i >= 0; --i){
        if(Balls[i] == 'B') sign = true;
        else if(sign) cnt++;
    }
    result = cnt;

    //빨간색을 오른쪽으로 옮기는 경우
    sign = false; cnt = 0;
    for(int i = 0; i < N; ++i){
        int cnt2 = 0;
        if(Balls[i] == 'B') sign = true;
        else if(sign) cnt++;
    }
    result = min(result,cnt);

    //파란색을 왼쪽으로 옮기는 경우
    sign = false; cnt = 0;
    for(int i = N-1; i >= 0; --i){
        if(Balls[i] == 'R') sign = true;
        else if(sign) cnt++;
    }
    result = min(result,cnt);

    //파란색을 오른쪽으로 옮기는 경우
    sign = false; cnt = 0;
    for(int i = 0; i < N; ++i){
        if(Balls[i] == 'R') sign = true;
        else if(sign) cnt++;
    }
    result = min(result,cnt);

    cout << result;
}