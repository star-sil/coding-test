/**
토마토

**/

#include <iostream>
#include <queue>

using namespace std;
typedef pair<int,int> ii;

int N, M, cnt, tomatos[1000][1000];
queue<ii> tomato;

int main(){
    std::ios::sync_with_stdio(false);
    ios.tie(0);

    cin >> M >> N;

    //만약 익은 사과가 있으면 다음에 익을 사과리스트에 대입
    for(int i = 0; i < N; ++i){
        for(int j = 0; j < M; ++j){
            cin >> tomatos[i][j];
            if(tomatos[i][j] == 1){
                tomato.push(ii(i+1,j)); tomato.push(ii(i-1,j));
                tomato.push(ii(i,j+1)); tomato.push(ii(i,j-1));
            }
        }
    }

    //익을 사과리스트가 없어질때까지 bfs 탐색
    while(!tomato.empty()){
        cnt++; int len = tomato.size();
        for(int i = 0; i < len; ++i){
            ii xy = tomato.front(); tomato.pop();
            if(tomatos[xy.first][xy.second] == 0 && xy.first >= 0 && xy.first < N && xy.second >= 0 && xy.second < M){
                tomatos[xy.first][xy.second] = 1;
                tomato.push(ii(xy.first+1,xy.second));
                tomato.push(ii(xy.first-1,xy.second));
                tomato.push(ii(xy.first,xy.second+1));
                tomato.push(ii(xy.first,xy.second-1));
            }
        }
        len = tomato.size();
    }

    //안익은 사과가 있는지 탐색
    for(int i = 0; i < N; ++i)
        for(int j = 0; j < M; ++j)
            if(tomatos[i][j] == 0) cnt = 0;

    cout << cnt - 1;
}