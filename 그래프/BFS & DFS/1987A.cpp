/**
알파벳
방문한 즉시 방문했다고 처리하면 추후에 다른 노드들이 방문을 못함 -> 해당 노드만 방문했다고 처리하기 위해
다음 방문을 하려하기 전에 방문했다고 처리하고 다시 방문을 안했다고 설정한다..

++

graph는 전역 변수 이므로 모든 노드들이 방문여부를 공유한다. 따라서 하나의 노드가 방문해서 방문 처리를하면
다른 노드는 방문을 안했어도 해당 좌표에 방문을 한 것으로 된다.
**/

#include <iostream>
using namespace std;

int R,C,result;
char graph[20][20];
bool visited[26];

void dfs(int x, int y, int cnt){
    int index = graph[x][y] - 'A';
    result = (cnt > result) ? cnt : result;

    if(x < R && x >= 0 && y < C && y >= 0 && !visited[index] && graph[x][y] != 0){
        cnt++; visited[index] = true;
        
        dfs(x+1,y,cnt); dfs(x,y+1, cnt); dfs(x-1,y, cnt); dfs(x,y-1,cnt);
        
        visited[index] = false;
    }
}

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> R >> C;
    for(int i = 0; i < R; ++i){
        for(int j = 0; j < C; ++j){
            cin >> graph[i][j];
        }
    }

    dfs(0,0,0);

    cout << result;
}