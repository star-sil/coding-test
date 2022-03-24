/**
컵라면

최악의 경우 O(n^2) 따라서 우선순위 큐 사용해야된다.
**/
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
typedef pair<int,long long> ii;

int N, maxDay; 
long long cnt;
vector<ii> cups;
priority_queue<int,vector<int>> pq;

int main(){
    cin >> N;

    for(int i = 0; i < N; ++i){
        int d; long long c; cin >> d >> c;
        maxDay = max(maxDay,d);
        cups.push_back(ii(d,c));
    }

    sort(cups.begin(),cups.end());

    int index = cups.size() - 1;
    for(int i = maxDay; i > 0; --i){
        //O(logN)
        while(!cups.empty()){
            if(cups[index].first == i){
                cout << i << " " << cups[index].first << " " << cups[index].second << "\n";
                pq.push(cups[index].second);
                index--;
            }
            else break;
        }
        if(!pq.empty()){
            cout << pq.top() << "\n";
            cnt += pq.top();
            pq.pop();
        } 
    }

    cout << cnt;
}