/**
배

시간초과가 뜬다.... 그냥 while문을 두고 일일이 비교하면 O(N*M^2)

++
벡터 자료형은 중간 원소를 제거할 수 있다. O(NMlogM)
**/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, crains[50], cnt, check;
vector<int> boxes;

int main(){
    cin >> N;
    for(int i = 0; i < N; ++i){
        cin >> crains[i];
    }

    cin >> M;
    for(int i = 0; i < M; ++i){
        int tmp; cin >> tmp;
        boxes.push_back(tmp);
    }

    sort(crains,crains + N);
    sort(boxes.begin(),boxes.end(),greater<int>());

    if(crains[N-1] < boxes[0]){
        cout << -1;
        return 0;
    }

    while(!boxes.empty()){
        cnt++;
        for(int i = 0; i < N; ++i){
            for(int j = 0; j < boxes.size(); ++j){
                if(crains[i] >= boxes[j]){
                    boxes.erase(boxes.begin()+j);
                    break;
                }
            }
        }
    }

    cout << cnt;
}
