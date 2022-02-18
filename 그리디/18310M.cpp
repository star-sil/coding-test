//안테나
#include <iostream>
#include <algorithm>

using namespace std;

int homes[200000], N, center;

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    for(int i = 0; i < N; ++i)
        cin >> homes[i];

    sort(homes, homes + N);

    if(N % 2 == 0) center = N / 2 -1;
    else center = N / 2;
    
    cout << homes[center];
    return 0;
}