/**
수 묶기

양수와 나머지로 나누어서 계산한다.
양수인 경우
두개를 묶을 수 있는 경우 큰수부터 차례로 두개씩 묶는다.
단 1과 다른 수가 함께 묶일 경우에는 묶지 않는 경우보다 작기 때문에 두개를
더한경우와 곱한경우를 비교해서 더 큰 방식을 채용한다.

나머지
나머지는 0 아니면 음수이기때문에 두개를 묶을 수 있는 경우 무조건 묶는 것이 좋다. 따라서 가장 작은 수 부터 두개씩 묶는다.
**/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<int> minusv, plusv, result;

int main(){
    cin >> N;
    for(int i = 0; i < N; ++i){
        int tmp; cin >> tmp;
        if(tmp > 0) plusv.push_back(tmp);
        else minusv.push_back(tmp);
    }

    sort(minusv.begin(), minusv.end(), greater<int>());
    sort(plusv.begin(), plusv.end());

    while(!minusv.empty()){
        if(minusv.size() == 1){
            result.push_back(minusv.back());
            minusv.pop_back();
        }
        else{
            int v1 = minusv.back(); minusv.pop_back();
            int v2 = minusv.back(); minusv.pop_back();
            result.push_back(v1 * v2);
        }
    }

    while(!plusv.empty()){
        if(plusv.size() == 1){
            result.push_back(plusv.back());
            plusv.pop_back();
        }
        else{
            int v1 = plusv.back(); plusv.pop_back();
            int v2 = plusv.back(); plusv.pop_back();
            if(v1*v2 > v1+v2) result.push_back(v1 * v2);
            else result.push_back(v1 + v2);
        }
    }

    int out = 0;
    for(int v : result){
        out += v;
    }

    cout << out;
}