/**
햄버거 분배
**/

#include <iostream>

using namespace std;

int N, K, result, sign;
char bench[20000];

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> K;
    for(int i = 0; i < N; ++i){
        cin >> bench[i];
    }

    int result = 0;
    for(int i = 0; i < N; ++i){
        if(bench[i] == 'P'){
            bool sign = false;
            for(int j = K; j > 0; --j){
                if(bench[i-j] == 'H'){
                    bench[i-j] = 0;
                    sign = true;
                    result++;
                    break;
                }
            }
            if(!sign){
                for(int j = 1; j <= K; ++j){
                    if(bench[i+j] == 'H'){
                        bench[i+j] = 0;
                        sign = true;
                        result++;
                        break;
                    }
                }
            }
        }
    }

    cout << result;
}