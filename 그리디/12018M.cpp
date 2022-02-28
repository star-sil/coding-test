/**
Yonsei TOTO

함정!!
수강인원이 수강가능인원보다 부족해도 마일리지 1점은 넣어야 한다.
각 강의의 마일리지 리스트를 내림차순으로 해서 마지막 부분을 넣어야 한다.
**/

#include <iostream>
#include <algorithm>

#define MAX 999;

using namespace std;

int N, M, P, L,cnt,result[100];

bool DESC(int a, int b){
    return a > b;
}

int main(){
    cin >> N >> M;
    for(int i = 0; i < N; ++i){
        cin >> P >> L;
        int diff = P - L;
        //수강인원이 수강가능인원보다 적을경우
        if(diff < 0){
            if(M - 1 >= 0){
                M -= 1;
                cnt++;
            }
            for(int j = 0; j < P; ++j){
                cin >> result[i];
                result[i] = MAX;
            }
        }
        //수강인원이 수강가능인원보다 같거나 많을경우
        else{
            int tmp[100];
            for(int j = 0; j < P; ++j){
                cin >> tmp[j];
            }

            sort(tmp,tmp+P,DESC);
            result[i] = tmp[L-1];
        }
    }

    sort(result,result+N);

    for(int i = 0; i < N; ++i){
        if(M >= result[i]){
            M -= result[i];
            cnt++;
        }
    }

    cout << cnt;
}