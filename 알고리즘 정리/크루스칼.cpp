//1922번 네트워크 연결(크루스칼 알고리즘)
// 크루스칼 알고리즘

#include <iostream>
#include <queue>

using namespace std;

int N, M;
int a, b, c;
int parent[1001];

struct Data {
    int node1, node2, weight;
    Data() {};
    Data(int node1, int node2, int weight) : node1(node1), node2(node2), weight(weight) {};

    bool operator<(const Data d) const {
        return weight > d.weight;
    }
};

int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

void uni(int x, int y) {
    parent[find(x)] = find(y);
}

int main(int argc, char** argv) {

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int count;
    int answer;
    priority_queue<Data> pq;

    cin >> N;
    cin >> M;

    for (int i = 0; i <= N; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < M; i++) {
        cin >> a >> b >> c;
        pq.push(Data(a, b, c));
    }

    count = 0;
    answer = 0;

    while (true) {
        if (count == N - 1) break;
        Data d = pq.top();
        pq.pop();
        if (find(d.node1) != find(d.node2)) {
            uni(d.node1, d.node2);
            count++;
            answer += d.weight;
        }
    }

    cout << answer;

    return 0;
}