/**
택배


**/

#include <iostream>
#include <algorithm>

using namespace std;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;

int N, C, M, result;
iii boxes[10000];
int truck[2001];


bool Custom(iii a, iii b){
    if(a.second.first == b.second.first) return a.first < b.first;
    else return a.second.first < b.second.first;
}

int main(){
    cin >> N >> C;
    cin >> M;

    for(int i = 0; i < M; ++i){
        int t,r,b;
        cin >> t >> r >> b;
        boxes[i] = iii(t,ii(r,b));
    }

    sort(boxes,boxes+M,Custom);

    for(int i = 0; i < M; ++i){
        int maxBox = 0;
        int start = boxes[i].first;
        int end = boxes[i].second.first;
        int cap = boxes[i].second.second;

        //배달 하는 마을을 부터 목적지까지 쌓인 택배수 확인(가장 큰 것 선택)
        for(int j = start; j < end; ++j){
            maxBox = max(maxBox, truck[j]);
        }

        //용량 - 현재 경로에 걸치는 마을중 가장 큰 택배수 만큼 가져갈 수 있다.
        maxBox = min(C-maxBox,cap);
        result += maxBox;

        for(int j = start; j < end; ++j){
            truck[j] += maxBox;
        }
    }

    cout << result;
}