/**
삼각형 만들기

두변의 길이가 한변의 길이보다 커야한다.
**/

#include <iostream>
#include <algorithm>

using namespace std;

int N, lines[1000000], result = -1;

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    
    cin >> N;
    for(int i = 0; i < N; ++i) cin >> lines[i];

    sort(lines,lines+N);

    for(int i = N-1; i >= 0; --i){
        if(i < 2) break;
        if(lines[i] < lines[i-1] + lines[i-2]){
            result = lines[i] + lines[i-1] + lines[i-2];
            break;
        } 
    }

    cout << result;
}

