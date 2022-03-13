/**
공유기 설치

공유기의 위치에 초점을 맞추는 것이 아닌 가장 최적의 간격에 초점을 맞춰야 한다.

간격을 1일때 2일때...등등의 맞게 설치할 수 있는 공유기를 차례로 계산해 최적의 간격을 알아내면 시간초가
따라서 이분탐색으로 최적의 거리를 찾아야 한다.
**/
#include <iostream>
#include <algorithm>

using namespace std;

int N, C ,homes[200000];

int main(){
    cin >> N >> C;
    for(int i = 0; i < N; ++i){
        cin >> homes[i];
    }

    sort(homes,homes + N);

    int left = 1; int right = homes[N-1] - 1;
    while(left <= right){
        int mid = (left + right) / 2;
        int start = homes[0];
        int cnt = 1;
        for(int i = 1; i < N; ++i){
            if(homes[i] - start >= mid){
                start = homes[i];
                cnt++;
            }
        }
        if(cnt < C){
            right = mid - 1;
        }
        else{
            left = mid + 1; 
        }
    }

    cout << right;
}