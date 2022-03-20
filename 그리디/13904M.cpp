/**
과제

최대 가능한 마감일부터 거꾸로 내려간다. 그리고 마감일에 맞는 과제중에 가장 큰 점수를 가진 과제를 선정한다.
과제를 찾았으면 해당 원소를 지운다.
과제일을 1부터 시작하면 우선순위의 기준을 정하기 힘들다. 날짜로 기준을 잡으면 과제 점수가 낮아지고 과제 점수를 기준으로
기준을 잡아도 최대 점수를 충족하다는 것을 보장하기 힘들다. 반대로 과제마감일을 거꾸로하면 마감일 기준으로 최대점수인 과제를
선택하면 되기때문에 최대 점수를 보장할 수 있다.

++
우선순위 큐 사용가능
**/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int,int> ii;

int N, maxDay, score;
vector<ii> homeworks;

bool Custom(ii a, ii b){
    return a.second > b.second;
}

int main(){
    cin >> N;

    for(int i = 0; i < N;++i){
        int d, w; cin >> d >> w;
        if(maxDay <= d) maxDay = d;
        homeworks.push_back(ii(d,w));
    }

    sort(homeworks.begin(),homeworks.end(),Custom);

    for(int i = maxDay; i > 0; --i){
        for(int j = 0; j < homeworks.size(); ++j){
            if(homeworks[j].first >= i){
                score += homeworks[j].second;
                homeworks.erase(homeworks.begin() + j);
                break;
            }
        }
    }

    cout << score;
}