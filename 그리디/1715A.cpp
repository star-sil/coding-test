/**
카드 정렬하기

벡터를 사용해 정렬하면 시간 초과가 된다.
따라서 우선순위 큐를 사용했는데
두 자료형의 시간복잡도 차이가 생기는지 알아보자
**/

#include <iostream>
#include <queue>

using namespace std;

priority_queue<int, vector<int>, greater<int> > pq;
int N, sum;

int main(void){
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    for (int i = 0; i < N; i++) {
        int n; cin >> n; pq.push(n);
    }

    while(pq.size() > 1) {
        int n1, n2;
        n1 = pq.top(), pq.pop();
        n2 = pq.top(), pq.pop();
        sum += (n1 + n2);
        pq.push(n1 + n2);
    }

    cout << sum;
    return 0;
}