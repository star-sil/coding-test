//행렬 곱셈 순서
#include <iostream>
#include <algorithm>
#define INF 987654321

using namespace std;

int N;
int m[500][2];
int dp[500][500];

int dfs(int x, int y){

    if(x == y) return 0;
    if(dp[x][y] != INF) return dp[x][y];

    for(int i = x; i < y; i++){
        dp[x][y] = min(dp[x][y], dfs(x, i) + dfs(i + 1, y) + m[x][0] * m[i][1] * m[y][1]);
    }
    return dp[x][y];
}

int main(int argc, char** argv){

    scanf("%d", &N);

    for(int i = 0; i < N; i++){
        scanf("%d %d", &m[i][0], &m[i][1]);
        for(int j = 0; j < N; j++){
            dp[i][j] = INF;
        }
    }

    printf("%d\n", dfs(0, N - 1));
    return 0;
}