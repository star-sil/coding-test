/**
A와 B

맨 마지막 문자를 만들기 위한 방법은 유일하다.

++
뒤집다라는 표현을 잘못 이해했다.
뒤집는다는건 A를 B로 바꾸는 그런게 아니라 AB면 BA로 바꾸는것을 뒤집는것으로 한다.

++
문자열 라이브러리 pop_back(), reverse() 숙지 
**/

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string S, T;
int result;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	cin >> S;
	cin >> T;

	while (1) {
		if (S.size() == T.size()) {
			if (S == T)
				result = 1;
			break;
		}
		
		if (T[T.size() - 1] == 'A')
			T.pop_back();
		else {
			T.pop_back();
			reverse(T.begin(), T.end());
		}
	}

	cout << result;
}