/**
물병

**/

#include <iostream>
#include <cmath>

using namespace std;

#define MAX 25

int N, K, sqaureArr[MAX];

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> K; int value = 0;
    for(int i = 0; value <= 10000000; ++i){
        value = pow(2,i);
        sqaureArr[i] = value;
    }

    int index = MAX - 1;
    while(true){
        if(K == 1){
            if(sqaureArr[index] < N){
                cout << sqaureArr[index+1] - N; break;
            }
            else if(sqaureArr[index] == N){
                cout << sqaureArr[index] - N; break;
            }
            index--; continue;
        }
        else{
            if(sqaureArr[index] < N){
                N -= sqaureArr[index]; K--;
                index = 24; continue;
            }
            else index--; 
        }
    }
}
