#include <bits/stdc++.h>

using namespace std;

#define MAXN 1000
int Arr[MAXN];

int binarySearch(int* arr, int size, int key)
{
    int lb = -1, ub = size-1, m;
    while(lb+1 < ub)
    {
        m = lb+(ub-lb)/2;
        if(arr[m] >= key) ub = m;
        else lb = m;
    }

    return ub>=size? -1 : arr[ub]==key? ub : -1 ;
}

int binarySearch2(int* arr, int size, int key)
{
    int *p = lower_bound(arr, arr+size, key);
    return (p-arr)>=size? -1 : *p==key? (p-arr) : -1 ;
}

int main()
{
    int t, T, N, M, key;
    scanf("%d", &T);
    for(t=1; t<=T; t++)
    {
        printf("#%d", t);
        scanf("%d %d", &N, &M);
        for(int i=0; i<N; i++) scanf("%d", &Arr[i]);
        for(int i=0; i<M; i++)
        {
            scanf("%d", &key);
            printf(" %d", binarySearch(Arr, N, key));
        }
        printf("\n");
    }
    return 0;
}