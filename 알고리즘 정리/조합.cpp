//순열 vs 조합
//https://www.geeksforgeeks.org/combinations-with-repetitions/

https://visualgo.net/en/recursion
//visual algol에서 사용하는 custom함수 및 파라메터
// s = 1, n = 5, m=3, top=0
// int f(int s, int n, int m, int top)
// {
//     if (top == m) return s-1; /* base case */
//     /* recursive caseS */
//     for (var i = s; i <= n; i++)
//     {
//     if(n-i+1 < m-top) break;//가지치기
//         top++;    
//         f(i+1,n,m,top);
//         top--;
//     }
//     return s-1;
// }


#include <bits/stdc++.h>

#define MAXN 10

using namespace std;

int N, M;
int Top;
int D[MAXN];

void printD()
{
    for(int i=0; i<M; i++) printf("%d ", D[i]);
    printf("\n");
}

void backtracking(int start)
{
    if(Top == M)
    {
        printD();
        return;
    }

    for(int i=start; i<=N; i++)
    {
        if(N-i+1 < M-Top) break;//가지치기
        D[Top++] = i;
        backtracking(i+1);
        Top--;
    }
}

int main()
{
    printf("combination\n");
    N = 5;
    M = 3;
    Top = 0;
    backtracking(1);

    return 0;
}