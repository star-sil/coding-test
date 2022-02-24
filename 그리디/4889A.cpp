/**
안정적인 문자열

반례: {}}{{} 정답: 2 출력: 0
**/

#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

vector<char> caseSet;

int main(){
    std::ios::sync_with_stdio(0);
    cin.tie(0);

    int num = 1;
    while(true){
        string caseArr; cin >> caseArr; int cnt = 0;

        if(caseArr[0] == '-') break;

        for(int i = 0; i < caseArr.length(); ++i){
            if(caseSet.empty() && caseArr[i] == '}'){
                caseArr[i] = '{'; cnt++;
            }
            if(caseArr[i] == '{'){
                caseSet.push_back(caseArr[i]);
            }
            else{
                caseSet.pop_back();
            }
        }

        if(!caseSet.empty()) cnt += (caseSet.size() / 2);

        cout << num << ". " << cnt << "\n";
        caseSet.clear(); num++;

    }
}