/**
피보나치

구하고자 하는 결과가 피보나치 수열에 속해있을때의 경우의 수도 파악해야한다.
그럼 결과는 하나가 나오게 되고 굳이 수열의 원소들을 더하지 않아도 원소 그자체가 답이 되므로
36번줄에서 부등호는 같거나 작은게 되어야한다.
**/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int fifoArr[44];

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    int f1 = 0; int f2 = 1; int max = 0;
    for(int i = 0; max < 1000000000; ++i ){
        max = f1 + f2;
        fifoArr[43-i] = max;
        f1 = f2; f2 = max;
    }

    int T; cin >> T;
    for(int t = 0; t < T; t++){
        int N; cin >> N;
        bool sign = false; long long result = 0; vector<int> vect;

        for(int v : fifoArr){
            if(v <= N) sign = true;
            if(sign == true){
                if(result + v <= N){
                    result += v;
                    vect.push_back(v);
                }
            }
            if(result == N) break;
        }
        
        sort(vect.begin(),vect.end());
        
        for(int v : vect) cout << v << " ";
        cout << "\n";
    }
    return 0;
}