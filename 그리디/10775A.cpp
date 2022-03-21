/**
공항

union find로 풀어야한다. union find 자료구조에 대한 이해 필요
**/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int G, P;
int parent[100001];

int find(int u) {
	if (parent[u] == u)return u;
	return parent[u] = find(parent[u]);
}

void Union(int u, int v) {
	u = find(u);
	v = find(v);
	parent[u] = v;
}

int main()
{
	cin >> G >> P;
	for (int i = 1; i <= G; i++) parent[i] = i;

	int g;
	int res = 0; 

	while (P--) {
		cin >> g;
		if (find(g) == 0) break;
		else {
			res++;
			Union(find(g), find(g) - 1);
		}
	}
	cout << res;
}