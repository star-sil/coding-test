/**
저울

오름차순으로 정렬 후 차례대로 더하는데 현재 더한 값은 지금까지 더한 원소들을
이용해 얻을 수 있는 가장 큰 수이다. 따라서 현재 더한 값보다 큰 값이 다음 원소로 주어지면
현재 더한 값의 +1이 정답이 된다.

수학적으로 접근해야됐음.....
**/

#include <iostream>
#include <algorithm>

using namespace std;

int N, weight[1000];
int main(){
    cin >> N;
    for(int i = 0; i < N; ++i){
        int tmp; cin >> tmp;
        weight[i] = tmp;
    }

    sort(weight,weight+N);

    int result = 1;

    for(int i = 0; i < N; ++i){
        if(weight[i] > result) break;
        result += weight[i];
    }

    cout << result;
}