/**
안정적인 문자열

반례: {}}{{} 정답: 2 출력: 0
**/

#include <iostream>
#include <cstring>

using namespace std;


int main(){
    std::ios::sync_with_stdio(0);
    cin.tie(0);

    int Num = 1;
    while(true){
        string caseArr; cin >> caseArr;
        int cnt1 = 0; int cnt2 = 0; int cnt3 = 0;
        if(caseArr[0] == '-') break;
        if(caseArr[0] == '}'){
            cnt1++;
        }
        if(caseArr[caseArr.length()-1] == '{'){
            cnt1++;
        }
        for(int i = 1; i < caseArr.length()-1; ++i){
            if(caseArr[i] == '{') cnt2++;
            else cnt3++;
        }

        cout << Num << ". " << abs(cnt3 - cnt2) / 2 + cnt1 << "\n";
        Num++;
    }
}