//1717 집합의 표현
#include <iostream>

using namespace std;

//전역변수를 사용하고 main에서 초기화 하는게 속도가 빠름
int n, m;
int cmd, a, b;
int parent[1000001];

//경로 압축기능도 가지고 있다.
int find(int x)
{
    //부모가 자기자신으면 자신은 리턴
    if(parent[x] == x) return x;
    //부모가 자신이 아니면 자신의 부모를 찾는다.
    return parent[x] = find(parent[x]);
}


void uni(int x, int y){
    parent[find(x)] = find(y);
}

int main(){
    //cin의 속도를 높이기 위해서 사용한다. 밑의 두줄
    //하지만 이걸 사용하면 cin만 사용해야됨 scanf 사용 x
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for(int i = 0; i <= n ; i++){
        parent[i] = i;
    }
    for(int i = 0; i < m; i++){
        cin >> cmd >> a >> b;
        if(cmd == 0){
            uni(a,b);
        }
        else{
            if(find(a) == find(b)){
                cout << "YES\n"
            }
            else{
                count << "NO\n"
            }
        }
    }
}