//카드 합체 놀이
//자료형 추가 조심!! int 20억이 넘어가면 long long을 사용
#include <bits/stdc++.h>
using namespace std;

long long Cards[1001];
int n,m;
long long sum;

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m;

    for(int i = 0; i < n; ++i){
        cin >> Cards[i];
    }

    for(int i = 0; i < m; ++i){
        sort(Cards,Cards + n);
        long long copy = Cards[0] + Cards[1];
        Cards[0] = Cards[1] = copy;
        
    }

    for(auto compo : Cards)
        sum += compo;
    
    cout << sum;
}