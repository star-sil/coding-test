//보물
#include <bits/stdc++.h>
using namespace std;
#define max 50

int arrA[max], arrB[max], N, result;


bool AscenSort(int a, int b){
    return a < b;
}

bool DescSort(int a, int b){
    return a > b;
}

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> N;

    for(int i = 0; i < N; ++i)
    {
        int tmp; cin >> tmp;
        arrA[i] = tmp;
    }
    for(int i = 0; i < N; ++i)
    {
        int tmp; cin >> tmp;
        arrB[i] = tmp;
    }

    sort(arrA,arrA+N,AscenSort); sort(arrB,arrB+N,DescSort);

    for(int i = 0; i < N; ++i)
    {
        result += arrA[i] * arrB[i];
    }
    cout << result;
}