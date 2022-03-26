/**
숫자구술

가장 큰 수를 기준으로 이진탐색을 통해 그룹의 최대값을 구한다.
하지만 그룹의 속한 원소를 출력할때 최대값으로 그룹을 생성해서 원소의 개수를 파악하면
각 그룹의 개수가 알맞지 않을 수 있기 때문에 적어도 한개를 생성할 수 있도록한다.
**/

#include <iostream>
#include <vector>

using namespace std;

int N, M, balls[300], minBall, totalBall;

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;

    for(int i = 0; i < N; ++i){
        cin >> balls[i];
        minBall = max(minBall,balls[i]);
        totalBall += balls[i];
    }

    int left = minBall;
    int right = totalBall;
    while(left <= right){
        int mid = (left + right) / 2;
        int groupCount = 1;
        int groupValue = 0;

        for(int i = 0; i < N; ++i){
            if(groupValue + balls[i] <= mid){
                groupValue += balls[i];
            }
            else{
                groupValue = balls[i];
                groupCount++;
            }
        }

        if(groupCount <= M){
            right = mid - 1;
        }
        else{
            left = mid + 1;
        }
    }

    cout << left << "\n";

    int count = 0; int value = 0;
    for(int i = 0; i < N; ++i){
        if(value + balls[i] <= left){
            value += balls[i];
            count++;
            if(N-i == M){
                cout << count << " ";
                i++;
                while(i < N){
                    cout << 1 << " ";
                    i++;
                }
            }
        }
        else{
            M--;
            value = balls[i];
            cout << count << " ";
            count = 1;
            if(N-i == M){
                while(i < N){
                    cout << 1 << " ";
                    i++;
                }
            }
        }
    }
}