/**
동전 뒤집기

**/
#include <iostream>

using namespace std;

int N, result = 401;
char coin[20][20];

int reverse(int row){
    int cnt1 = 0, cnt2 = 0;
    for(int i = 0; i < N; ++i){
        if(coin[row][i] == 'T') coin[row][i] = 'H';
        else coin[row][i] = 'T';
    }

    for(int i = 0; i < N; ++i){
        for(int j = 0; j < N; ++j){
            if(coin[i][j] == 'T') cnt1++;
            cout << coin[i][j] << "";
        }
        cout << "\n";
    }
    cout << "\n";

    for(int i = 0; i < N; ++i){
        if(coin[row][i] == 'T') coin[row][i] = 'H';
        else coin[row][i] = 'T';
    }

    for(int i = 0; i < N; ++i){
        if(coin[i][row] == 'T') coin[i][row] = 'H';
        else coin[i][row] = 'T';
    }

    for(int i = 0; i < N; ++i){
        for(int j = 0; j < N; ++j){
            if(coin[i][j] == 'T') cnt2++;
            cout << coin[i][j] << "";
        }
        cout << "\n";
    }
    cout << "\n";

    for(int i = 0; i < N; ++i){
        if(coin[i][row] == 'T') coin[i][row] = 'H';
        else coin[i][row] = 'T';
    }
    return min(cnt1,cnt2);
}


int main(){
    cin >> N;

    for(int i = 0; i < N; ++i){
        for(int j = 0; j < N; ++j){
            cin >> coin[i][j];
        }
    }

    for(int i = 0; i < N; ++i){
        int cnt = reverse(i);
        cout << cnt << "\n";
        if(result >= cnt) result = cnt;
    }

    cout << result;
}