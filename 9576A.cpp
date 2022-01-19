//책 나눠주기
//반례를 찾지 못함
//테스트 케이스에서 초기화를 시켜주지 못했다.
//visited 배열의 길이가 1000이 아니라 1001이되어야한다.
//size 잘못 찾았다.
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
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
        int M, N; scanf("%d %d",&N,&M);
        vii AL;
        memset(arr,0,sizeof(arr));
        for(int j = 0; j < M; ++j){
            int a, b; scanf("%d %d", &a, &b);
            AL.push_back(ii(a,b));
        }
        sort(AL.begin(),AL.end(),compare);
        for(int j = 0; j < M; ++j)
        {
            int n = AL[j].first;
            int m = AL[j].second;
            for(int k = n; k <= m; ++k){
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