#include <iostream>
#include <vector>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
using namespace std;
int main()
{
    vector<int> v3 = {1,2,3,4,5};

    v3.push_back(6); //뒤에 원소 추가
    v3.front(); //맨 앞에 원소
    v3.end(); //맨 뒤에 원소
    v3.size();
    v3.empty(); //비어있는지 검사
    //v3.insert(자리, 삽입할 원소) 배열 삽입도 가능
    //v3.clear(); 벡터 비우기
    v3.pop_back(); //뒤에 원소 제거

    //pair 두 자료형을 하나의 쌍으로 묶는다.
    pair<int,string> p1;
    //p1.first, p1.second; 첫번째 원소는 first 두번째 원소는 second
    pair<pair<int,string>,pair<int,int>> p2 = make_pair(make_pair(1,"hello"),make_pair(2,1)); //pair로 pair만들기 가능
    //p2.first.first
    //pair<string,int> p3 = pair<"hello",1>; 이렇게는 만들 수 없다!!


    //set 균형 이진트리로 구성, key값은 중복되지 않는다. , insert를 통해 입력하면 자동 정렬된다. 파이썬 딕셔너리 아님!!
    set<int> s;
    s.insert(10); s.insert(30); s.insert(20);
    s.find(30); //값 존재여부 확인

    //map: 파이썬 딕셔너리랑 비슷 set과 다르게 <key, value>의 쌍으로 저장, set처럼 컨테이너에 원소 key,value를 삽입하는 멤버 함수 insert()를 제공
    map<int,string>m;
    m.insert(pair<int,string>(2,"hello"));
    m.insert(pair<int,string>(5,"hey"));
    pair<int,string> tp(3,"haha"); //이런식으로 선언 가능
    m.insert(tp); 
    m[10] = "hi"; //이런식으로 키/값 넣을 수 있다.
    //m.insert(pair<int,int>(5,3)); 다른 데이터형의 pair 값 대입 불가!!

    
    //stack
    stack<int> st;
    st.push(3); st.push(4); st.push(5);
    st.pop(); //맨 뒤에 값 제거 반환 안함
    st.top(); //맨 뒤에 값 출력
    st.empty(); //비어있는지 확인
    st.size(); //스택 사이즈 반환

    //queue
    queue<int> q;
    q.push(3); q.push(4); q.push(5);
    q.pop(); //맨 앞에 값 제거 값을 반환하지는 않는다.
    q.front(); //맨 앞에있는 값 반환

    //priority queue 들어간 순서와 상관없이 우선순위가 높은 데이터가 먼저 나온다.
    priority_queue<int, vector<int>,less<int>> pq; //클수록 우선순위 높다.
    //priority_queue<int, vector<int>, greater<int>> pq; 작을 수록 우선순위 높다.
    pq.push(3); pq.push(4); pq.push(5);
    pq.pop(); //pop 우선순위가 높은 원소 제거
    pq.top(); //top 우선순위가 높은 원소를 반환
    pq.empty();
    pq.size();

}