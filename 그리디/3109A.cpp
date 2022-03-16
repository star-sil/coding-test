/**
빵집

완전 탐색으로 접근
방문 행렬과 map을 분리
방문 순서도 중요.....!! 왜 중요하지? 위 - 중간 - 아래 순으로가야지 그리디하게 풀 수 있다.
왜 check를 쓰는지.... 가스관에서 빵집으로 이동을 했으면 다음 가스관에서 탐색을 해야함으로
**/

#include <iostream>

using namespace std;

int R, C, cnt;
char map[10000][500];
bool visited[10000][500];
bool check;
//인덱스가 줄어들어야 위로 간다. 3 -> 2 -> 1
int dx[3] = {-1,0,1};
int dy[3] = {1,1,1};

void dfs(int x, int y){
    visited[x][y] = true;

    if(y == C-1){
        cnt++;
        check = true;
        return;
    }

    for(int i = 0; i < 3; ++i){
        int nx = x + dx[i]; int ny = y + dy[i];
        if(nx >= 0 && nx < R && ny >= 0 && ny < C && map[nx][ny] == '.' && visited[nx][ny] == false){
            if(check) return;
            dfs(nx,ny);
        }   
    }
}

int main(){
    cin >> R >> C;
    for(int i = 0; i < R; ++i){
        for(int j = 0; j < C; ++j){
            cin >> map[i][j];
        }
    }

    for(int i = 0; i < R; ++i){
        check = false;
        dfs(i,0);
    }

    cout << cnt;
}