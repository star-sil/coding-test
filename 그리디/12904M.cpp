/**
A와 B

맨 마지막 문자를 만들기 위한 방법은 유일하다.

++
뒤집다라는 표현을 잘못 이해했다.
뒤집는다는건 A를 B로 바꾸는 그런게 아니라 AB면 BA로 바꾸는것을 뒤집는것으로 한다.

++
문자열 라이브러리 pop_back(), reverse() 숙지 
**/
#include <iostream>
#include <cstring>

using namespace std;

string S, T;

int main(){
    cin >> S >> T;
    int diff = T.length() - S.length();
    for(int i = 0; i < diff; ++i){
        if(T[T.length()-1 - i] == 'A') T[T.length()-1-i] = '\0';
        else{
            T[T.length()-1-i] = '\0';
            for(int j = 0; j < (T.length()-1-i)/2; ++j){
                char tmp = T[j];
                T[j] = T[T.length()-2-i-j];
                T[T.length()-2-i-j] = tmp;
            }
        }
    }

    for(int i = 0; i < S.length(); ++i){
        if(S[i] != T[i]){
            cout << 0; return 0;
        }
    }

    cout << 1;
}