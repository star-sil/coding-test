//수리공 항승
//sort함수 벡터일때 배열일때 쓰는법 다름
//마지막 부분으로 다시 테이프 부착할 경우도 생각해야된다. -> 마지막 부분으로 다시 테이프를 부착할 경우는 이미 카운트 된다.
//왜냐하면 maxline을 넘어가면 테이프 갯수를 1개 증가시키기 때문 + 결과도 +1해줌으로써 처음 붙이는 경우를 계산함
#include <bits/stdc++.h>
using namespace std;
int N, L,maxline, check;
vector<int> pipe;


int main(){
    cin >> N >> L;
    for(int i = 0; i < N; ++i){
        int tmp; cin >> tmp;
        pipe.push_back(tmp);
    }

    sort(pipe.begin(),pipe.end());
    for(int i = 0; i < N;){
        maxline = pipe[i] + L;
        bool flag = false;
        for(int j = i+1; j < N; ++j){
            if(pipe[j] >= maxline){
                check++;
                i = j;
                flag = true;
                break;
            }
        }
        if(!flag) i++;
    }
    cout << check+1;
    return 0;
}