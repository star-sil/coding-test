/**
도서관

**/
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, M, arr[50], maxPlace, total;

int main(){
    cin >> N >> M;

    for(int i = 0; i < N; ++i){
        cin >> arr[i];
        maxPlace = max(maxPlace,abs(arr[i]));
    }

    sort(arr,arr+N);

    for(int i = 0; i < N; ++i){
        if(arr[i] > 0) break;
        if(i % M == 0) total += abs(arr[i]) * 2;
    }

    for(int i = N-1; i >=0; --i){
        if(arr[i] < 0) break;
        if((i - (N-1)) % M == 0) total += arr[i] * 2;
    }

    cout << total - maxPlace;

}