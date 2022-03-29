/**
성냥개비

dp[i] = dp[i-2]*10 + num[2]; 무슨 의미인지 이해 불가....
**/
#include <iostream>

using namespace std;

int T;
int small[9] = {0,0,1,7,4,2,0,8,10};
int dp[101];

int main(){
    cin >> T;

    for(int i = 0; i < 101; ++i){
        for(int i=1; i<9; i++){
            dp[i] = small[i];
        }
        dp[6] = 6;

        for(int i=9; i<101; i++){
            dp[i] = dp[i-2]*10 + num[2];

            for(int j=3; j<8; j++){
                dp[i] = min(dp[i], dp[i-j]*10 + small[j]);
            }
        }
    }

    for(int i = 0; i < T; ++i){
        int V; cin >> V;
        //작은거
        cout << dp[V] << " ";

        //큰거
        int bigResult = V;
        while(bigResult){
            if(bigResult % 2 == 1){
                cout << 7;
                bigResult -= 3;
            }
            else{
                cout << 1;
                bigResult -= 2;
            }
        }
        cout << "\n";
    }
}