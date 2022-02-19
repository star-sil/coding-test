//A -> B
//두가지 방법 2를곱하고 1을 가장오른쪽에 추가가 모두 불가능할 경우도 처리해줘야함 -1 출력으로
#include <bits/stdc++.h>
using namespace std;

int A, B, C,result;

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    
    cin >> A >> B;
    while (true){
        if(B != A && B < A){
            cout << -1;
            break;
        }
        else if(A == B){
            cout << result + 1;
            break;
        }

        if(B % 2 == 0) {
            B /= 2;
            result++;
            continue;
        }
        else if(B % 10 == 1){ 
            B /= 10;
            result++;
            continue;
        }
        else{
            cout << -1;
            break;
        }
    }
    return 0;
}
