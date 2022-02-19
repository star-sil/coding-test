#include <iostream>
#include <vector>
#include <queue>

#define INF 987654321

struct Data {
    int node;
    int weight;
    Data() {};
    Data(int node, int weight) : node(node), weight(weight) {};
    bool operator<(const Data d)const{
        return weight > d.weight;
    }
};

using namespace std;

vector<Data> v[10];
int dist[10];
bool isVisited[10];
int N,M;
int a, b, c;
priority_queue<Data> pq;

int main(){
    scanf("%d %d",&N,&M);

    for(int i = 0; i <= N; i++){
        v[i].clear();
        dist[i] = INF;
        isVisited[i] = false;
    }
    for(int i = 0; i < M; i++){
        //무방향 그래프일 경우에는 a에서 b를 갈 수 있고 b에서도 a를 살 수 있기 때문에
        scanf("%d %d %d",&a, &b, &c);
        v[a].push_back(Data(b,c));
        v[b].push_back(Data(a,c));
    }

    dist[1] = 0;
    pq.push(Data(1,0));

    while(true){
        if(pq.empty()) break;
        //지금 방문한 노드
        Data now = pq.top();
        pq.pop();

        if(isVisited[now.node]) continue;
        isVisited[now.node] = true;
        for(int i = 0; i < v[now.node].size(); i++){
            //다음 방문할 노드 정보
            Data next = v[now.node].at(i);
            if(dist[next.node] > dist[now.node] + next.weight){
                dist[next.node] = dist[now.node] + next.weight;
                pq.push(Data(next.node, dist[next.node]));
            }
        }
    }
    for(int i = 0; i < N; i++){
        printf("%d %d \n",i, dist[i]);
    }
    return 0;
}