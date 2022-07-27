/**
통나무 건너뛰기
**/

#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

int T, N, trees[10000], insert[10000];

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> T; 
    for(int i = 0; i < T; ++i){
        cin >> N;
        memset(trees,0,sizeof(trees)); memset(insert,0,sizeof(insert));
        for(int j = 0; j < N; ++j){
            cin >> trees[j];
        }

        sort(trees, trees + N);

        for(int j = 0; j < N;){
            insert[j / 2] = trees[j];
            if(insert[N-1-(j/2)] == 0) insert[N-1-(j/2)] = trees[j+1];
            j += 2;
        }

        int max = 0;
        for(int j = 1; j < N; ++j)
            max = max < abs(insert[j] - insert[j-1]) ? abs(insert[j] - insert[j-1]) : max;

        max = max < abs(insert[0] - insert[N-1]) ? abs(insert[0] - insert[N-1]) : max;

        cout << max << "\n";
    }

}