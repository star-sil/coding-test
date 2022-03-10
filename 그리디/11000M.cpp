/**
강의실 배정

가장 빨리 끝나는 강의 시간과 비교하고 넣어야 하는 이유...를 모르겠다...
**/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int,int> ii;

vector<ii> lectures,result;

int N, arr[200000];

bool sortLogic(ii a, ii b){
    if(a.second == b.second) return a.first < b.first;
    else return a.second < b.second;
}

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for(int i = 0; i < N; ++i){
        int v1, v2; cin >> v1 >> v2;
        lectures.push_back(ii(v1,v2));
    }

    sort(lectures.begin(),lectures.end());

    for(auto v : lectures){
        cout << v.second << "\n";
    }
    result.push_back(lectures[0]);

    for(int i = 1; i < N; ++i){
        ii compare = lectures[i];
        bool find = false;
        for(int j = 0; j < result.size(); ++j){
            if(result[j].second <= compare.first){
                result[j].second = compare.first;
                find = true;
                break;
            }
        }
        if(!find) result.push_back(compare);
    }

    cout << result.size();
    
}