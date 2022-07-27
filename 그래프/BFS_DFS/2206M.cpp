/**
벽 부수고 이동하기

cin으로 0000같은 입력 처리방법 찾기

저번주에 풀었던 문제와 유사한거같다.
++cnt를 함수안에 넣으면 다음 함수에 영향이 간다.
ex) dfs(cnt++); dfs(cnt++); 이런식이면 첫번째로 증가한 cnt가 다시 두번째 함수로 들어갈때 한번더 증가한다.
따라서 함수안에 ++연산자를 사용하지 말자 특히 재귀함수일때!!
**/

#include <iostream>
#include <cstdio>

using namespace std;

int N, M, wall[1000][1000];
int xList[4] = {1,0,-1,0};
int yList[4] = {0,1,0,-1};
int result = -1;


void dfs(int x, int y, int punch, int cnt){
    if(x == N-1 && y == M-1){
        if(result == -1) result = cnt;
        else result = min(result,cnt);
    }
    else if(x >= 0 && x < N && y >= 0 && y < M){
        if(wall[x][y] == 1 && punch < 1){
            //이렇게 for문 밖에서 초기화 시켜도 되는 이유는 하위 노드들이 모두 이 방문기록을 공유하기 때문이다.(트리구조이기 때문에)
            //하지만 punch나 cnt는 for문 안에서 증가시키면 안된다. 왜냐하면 하위노드들이 for문으로 반복해서 cnt나 punch를 증가시키기 때문이다.
            wall[x][y] = 2; punch++; cnt++;
            for(int i = 0; i < 4; ++i){
                if(x+xList[i] < 0 || x+xList[i] >= N || y+yList[i] < 0 || y+yList[i] >= N) continue;
                dfs(x+xList[i],y+yList[i],punch,cnt);
            }
            wall[x][y] = 1;
        }
        else if(wall[x][y] == 0){
            wall[x][y] = 2; cnt++;
            for(int i = 0; i < 4; ++i){
                if(x+xList[i] < 0 || x+xList[i] >= N || y+yList[i] < 0 || y+yList[i] >= N) continue;
                dfs(x+xList[i],y+yList[i],punch,cnt);
            }
            wall[x][y] = 0;
        }
    }
}

int main(){
    scanf("%d %d",&N,&M);

    for(int i = 0; i < N; ++i){
        for(int j = 0; j < M; ++j){
            scanf("%1d",&wall[i][j]);
        }
    }

    dfs(0,0,0,1);

    printf("%d",result);
    
    return 0;
}