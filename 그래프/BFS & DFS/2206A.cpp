/**
벽 부수고 이동하기

cin으로 0000같은 입력 처리방법 찾기

가중치 없는 최단거리는 bfs로 풀어야한다.

++
시간초과는 안뜨는데 이제 틀렸다. 반례가 뭐지.....??
직접 그리면서 해결해보자 B코드랑 비교하면서 반례는

6 3
000
110
000
011
111
000
**/

#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;
typedef pair<int,int> ii;
typedef pair<ii,ii> iiii;

int N, M, wall[1000][1000], visited[1000][1000][2];
int xList[4] = {1,0,-1,0};
int yList[4] = {0,1,0,-1};
int result = -1;
queue<iiii> doVisit;


int main(){
    scanf("%d %d",&N,&M);

    for(int i = 0; i < N; ++i){
        for(int j = 0; j < M; ++j){
            scanf("%1d",&wall[i][j]);
        }
    }

    int cnt = 0; int punch = 0;

    doVisit.push(iiii(ii(0,0),ii(0,1)));

    while(!doVisit.empty()){
        iiii node = doVisit.front(); doVisit.pop();
        ii xy = node.first; int x= xy.first; int y= xy.second;
        ii pc = node.second; int punch = pc.first; int cnt = pc.second;

        if(x == N-1 && y == M-1){
            if(result == -1) result = visited[x][y][punch];
            else result = min(result,cnt);
        }

        if(x >= 0 && x < N && y >=0 && y < M){
            if(wall[x][y] == 0 && !visited[x][y][0]){
                cnt++; visited[x][y][0] = cnt;
                doVisit.push(iiii(ii(x+1,y),ii(punch,cnt))); doVisit.push(iiii(ii(x-1,y),ii(punch,cnt)));
                doVisit.push(iiii(ii(x,y+1),ii(punch,cnt))); doVisit.push(iiii(ii(x,y-1),ii(punch,cnt)));
            }
            else if(wall[x][y] == 1 && punch < 1){
                cnt++; punch++; visited[x][y][punch] = cnt;
                doVisit.push(iiii(ii(x+1,y),ii(punch,cnt))); doVisit.push(iiii(ii(x-1,y),ii(punch,cnt)));
                doVisit.push(iiii(ii(x,y+1),ii(punch,cnt))); doVisit.push(iiii(ii(x,y-1),ii(punch,cnt)));
            }
            
        }
    }

    printf("%d",result);
    
    return 0;
}