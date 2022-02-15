//단어수학
//문자 연산 기능 숙지 https://dojang.io/mod/page/view.php?id=62
//문자열 입력 기능 및 활용 숙지(strlen)
#include <bits/stdc++.h>
using namespace std;

char words[10][10];
int alpha[26], result, N, len[10];

bool DESC(int a, int b){
    return a > b;
}

int main(){
    
    cin >> N;
    for(int i = 0; i < N; ++i){
        //문자열 입력 가능
        cin >> words[i];
        //문자열의 길이 파악 가능
        len[i] = strlen(words[i]);
    }

    for(int i = 0; i < N; ++i){
        int cal = 1;
        for(int j = len[i]-1; j >= 0; --j){
            //문자 연산을 통해 인덱스를 지정할 수 있다.
            alpha[words[i][j] - 'A'] += cal;
            cal *= 10;
        }
    }

    sort(alpha,alpha+26, DESC);

    for(int i = 0; i < 10; i++){
        result += alpha[i] * (9 - i);
    }

    cout << result;
}

