/*
특정한 최단 경로


*/


#include <iostream>
#include <vector>
#include <queue>
#define INF 987654321

using namespace std;
typedef pair<int,int> ii;

int N, M,v1,v2;
vector<ii> graph[801];
int trace[801];

vector<int> dijkstra(int start, int vertex)
{
    vector<int> distance(vertex, INF);
    distance[start] = 0;
    priority_queue<ii, vector<ii>, greater<ii>> pq;
    pq.push(ii(0,start));

    while(!pq.empty())
    {
        int cost = pq.top().first;
        int current = pq.top().second;
        pq.pop();

        for(int i = 0; i < graph[current].size(); i++){
            int next = graph[current][i].first;
            int nextCost = graph[current][i].second;

            if(distance[next] > cost + nextCost){
                distance[next] = cost + nextCost;
                trace[next] = current;
                pq.push(ii(distance[next],next));
            }
        }
    }
    return distance;
}

int main(){
    cin >> N >> M;
    N++;
    for(int i = 0; i < M; ++i){
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back(ii(b,c));
        graph[b].push_back(ii(a,c));
    }
    cin >> v1 >> v2;

    vector<int> result = dijkstra(1,N);
    vector<int> temp1 = dijkstra(v1,N);
    vector<int> temp2 = dijkstra(v2,N);

    //시작 -> v1 -> v2 -> result, 시작 -> v2 -> v1 -> result;
    int answer = min((result[v1] + temp1[v2] + temp2[N - 1]), (result[v2] + temp2[v1] + temp1[N - 1] ));
    if (answer >= INF || answer < 0)
        cout << -1 << "\n";
    else
        cout << answer << "\n";
    return 0;
}