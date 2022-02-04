//행렬
// int 변수 1과 0을 비트연산 &을 하게되면 0001 & 0000 => 0000
// 반대로 바꾸기 위해서는 xor연산을 해야한다.
// 반례에서 막혔다 + ios_base를 사용하면 scanf를 사용하면 안된다. 
#include <bits/stdc++.h>
using namespace std;

int arr[50][50];
int N,M,cnt;

int main(){
    cin >> N >> M;
    for(int i = 0; i < N; ++i)
        for(int j = 0; j < M; ++j)
            scanf("%1d",&arr[i][j]);

    for(int i = 0; i < N; ++i)
        for(int j = 0; j < M; ++j){
           int tmp; scanf("%1d", &tmp);
           arr[i][j] ^= tmp; //기존 행렬과 다른 경우 1 같은경우 0
        }  
    
    for(int i = 0; i < N; ++i)
        for(int j = 0; j < M; ++j){
            if(arr[i][j]){
                //바꿔야 하지만 범위가 넘어가는 경우 안된다고 판단
                if(i + 2 >= N || j + 2 >= M){
                    cout << -1;
                    return 0;
                }

                for(int k = i; k < i + 3; ++k){
                    arr[k][j] ^= 1;
                    arr[k][j+1] ^= 1;
                    arr[k][j+2] ^= 1;
                }

                cnt++;
            }
        }

    cout << cnt;
    return 0;
}