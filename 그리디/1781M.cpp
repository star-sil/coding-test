/**
컵라면

최악의 경우 O(n^2) 따라서 우선순위 큐 사용해야된다.
**/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int,long long> ii;

int N, maxDay; 
long long cnt;
vector<ii> cups;

bool Custom(ii a, ii b){
    if(a.second == b.second) return a.first < b.second;
    else return a.second < b.second;
}

int main(){
    cin >> N;

    for(int i = 0; i < N; ++i){
        int d; long long c; cin >> d >> c;
        if(maxDay < d) maxDay = d;
        cups.push_back(ii(d,c));
    }

    sort(cups.begin(),cups.end(),Custom);

    for(int i = maxDay; i > 0; --i){
        if(!cups.empty()){
            for(int j = cups.size()-1; j >= 0; --j){
                if(cups[j].first >= i){
                    cnt += cups[j].second;
                    cups.erase(cups.begin()+j);
                    break;
                }
            }
        }

    }

    cout << cnt;
}