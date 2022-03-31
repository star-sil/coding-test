/**
순회강연

최대 마감부터 앞으로 가면서 해당 마감안에 할 수 있는 공연들의 강의료를 우선순위 큐로 넣는다.
**/
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;
typedef pair<int,int> ii;

priority_queue<int,vector<int>> pq;
vector<ii> lectures;

int N, P, D, maxDay, result;

bool compare(ii a, ii b){
    if(a.second == b.second) return a.first < b.first;
    else return a.second < b.second;
}

int main(){
    cin >> N;

    for(int i = 0; i < N; ++i){
        cin >> P >> D;
        maxDay = max(maxDay,D);
        lectures.push_back(ii(P,D)); 
    }

    sort(lectures.begin(),lectures.end(),compare);

    for(int i = maxDay; i > 0; --i){
        while(!lectures.empty()){
            if(lectures.back().second >= i){
                pq.push(lectures.back().first);
                lectures.pop_back();
            }
            else break;
        }
        if(!pq.empty()){
            result += pq.top();
            pq.pop();
        }
    }
    cout << result;
}