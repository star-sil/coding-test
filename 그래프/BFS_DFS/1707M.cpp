/**
이분 그래프

인접하다 정의 : 정점 사이에 간선이 존재하면 인접하다.

반례
1
4 3
1 3
2 4
3 4

**/
#include <iostream>
using namespace std;

int K, V, E, vertax[200000];

#define NO 0
#define YES 1

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> K;
    for(int i = 0; i < K; ++i){
        bool a[200000] = {0,};
        bool b[200000] = {0,};
        cin >> V >> E;
        bool sign = false;
        for(int j = 0; j < E; ++j){
            int v1, v2; cin >> v1 >> v2;
            if(a[v1] == YES || b[v1] == YES){
                if(a[v1] == YES) b[v2] = YES;
                else if(b[v1] == YES) a[v2] = YES;
                if((a[v1] == YES && b[v1] == YES) || (a[v2] == YES && b[v2] == YES) ){
                    cout << "NO" << a[v2] << b[v2] <<  " "<< j<< "\n";
                    sign = true;
                    break;
                }
            }
            else{
                if(a[v2] == YES) b[v1] = YES;
                else if(b[v2] == YES) a[v1] = YES;
                else{
                    a[v1] = YES; b[v2] = YES;
                }
                if((a[v1] == YES && b[v1] == YES) || (a[v2] == YES && b[v2] == YES) ){
                    cout << "NO2" << "\n";
                    sign = true;
                    break;
                }
            }
            cout << a[1] <<  " " << a[2] << " " << a[3] << " " << a[4] << " "<<"\n";
            cout << b[1] <<  " " << b[2] << " " << b[3] << " " << b[4] << " "<<"\n";
                
            
            if((a[v1] == YES && b[v1] == YES) || (a[v2] == YES && b[v2] == YES) ){
                cout << "NO3" << "\n";
                sign = true;
                break;
            }
        }
        if(!sign) cout << "YES" << "\n";
    }
}