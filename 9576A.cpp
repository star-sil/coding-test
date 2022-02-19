//책 나눠주기
//반례를 찾지 못함
//테스트 케이스에서 초기화를 시켜주지 못했다.
//visited 배열의 길이가 1000이 아니라 1001이되어야한다.(index가 1부터 시작)
//웬만하면 전역변수로 선언하는게 좋다. 속도 증가
//mamset에서 size 잘못 입력해서 사이즈 잘못 초기화했다.
#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
vii AL;
int arr[1001];
int ct, T;

bool compare(ii a, ii b)
{
    if (!(a.second == b.second))
        return a.second < b.second;
    return a.first < b.first;
}

int main(){
    scanf("%d", &T);
    for(int i = 0; i < T; ++i)
    {
        vii AL; int M, N; scanf("%d %d",&N,&M);
        //배열과 벡터 초기화
        memset(arr,0,sizeof(arr)); AL.assign(M,ii(0,0));
        for(int j = 0; j < M; ++j){
            int a, b; scanf("%d %d", &a, &b);
            AL[j] = ii(a,b);
        }
        sort(AL.begin(),AL.end(),compare);
        for(int j = 0; j < M; ++j)
        {
            for(int k = AL[j].first; k <= AL[j].second; ++k){
                if(arr[k] == 0){
                    ct++;
                    arr[k] = 1;
                    break;
                }
            }
        }
        printf("%d\n",ct);
        ct = 0;
    }
    return 0;
}