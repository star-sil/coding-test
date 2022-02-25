/**
팔

자릿수가 맞지 않으면 무조건 0
자릿수가 맞으면 앞자리수부터 L은 R보다 무조건 작으므로 자릿수가 맞아도 둘다 8이 아니면 해당 자리수부터 뒷자리는 모두 8을 피할 수 있다.
따라서 앞부분부터 검사해서 둘다 8이나오면 카운트하고 둘다 8이 아니면 카운트를 중단하고 결과를 반환한다.
**/

#include <iostream>
#include <cstring>

using namespace std;

string L, R;

int main(){
    cin >> L >> R;

    std::ios::sync_with_stdio(false);
    cin.tie(0);

    int cnt = 0;
    if(L.length() == R.length()) {
        for(int i = 0; i < L.length(); ++i){
            if(L[i] != R[i]) break;
            else{
                if(L[i] == '8') cnt++;
            }
        }
    }
    cout << cnt;

    return 0;
}
