/**
카드 문자열

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
가장 빠른 문자열이라는 뜻
ex) M K U
M K U
U K M
K M U
K U M
M U K
U M K
가장 사전순으로 빠른것은 KMU
**/
#include <iostream>
#include <deque>

using namespace std;

char alpha[1000];
int T, N;

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    
    cin >> T;
    for(int t = 0; t < T; ++t){
        cin >> N; deque<char> result;;
        for(int i = 0; i < N; ++i){
            cin >> alpha[i];
        }

        for(int i = 0; i < N; ++i){
            if(i == 0) result.push_back(alpha[i]);
            else{
                if( alpha[i] - 'A' <= result.front() -'A') result.push_front(alpha[i]);
                else result.push_back(alpha[i]);
            }
        }

        for(int i = 0; i < result.size(); ++i)
            cout << result[i] << "";
        
        cout << "\n";
    }

}