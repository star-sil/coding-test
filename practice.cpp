#include <iostream>
#include <vector>
#include <iostream>
#include <string>
#include <set>
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


    //set 균형 이진트리로 구성, key값은 중복되지 않는다. , insert를 통해 입력하면 자동 정렬된다.


}