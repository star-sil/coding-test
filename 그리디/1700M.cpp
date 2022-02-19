//멀티탭 스케줄링
//먼저 플러그가 비어있거나 이미 있는경우를 체크하고 없는 경우에는
//꽂을 콘센트가 가장 멀리있거나 없는 플러그를 제거
//check max < k 조건문 안쪽에다가 해서 해당 콘센트가 플러그인에 존재해도 check가 안되는 현상이 생겼다.

#include <iostream>
using namespace std;
int N, K, result;
int useArr[100], plug[100];
int main()
{
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> N >> K;
    for(int i = 0; i < K; ++i)
        cin >> useArr[i];

    for(int i = 0; i < K; ++i)
    {
        bool plugin = false;
        for(int j = 0; j < N; ++j)
        {
            if(plug[j] == 0 || plug[j] == useArr[i])
            {
                plug[j] = useArr[i];
                plugin = true;
                break;
            }
        }

        if(plugin) continue;

        int max = -1; int index = 0;
        for(int j = 0; j < N; ++j)
        {
            bool check = false;
            for(int k = i; k < K; ++k)
            {
                if(plug[j] == useArr[k])
                {
                    check = true;
                    if(max < k) {
                        max = k;
                        index = j;
                    }
                    break;
                }
            }
            if(!check)
            {
                max = -1;
                index = j;
                break;
            }
        }
        plug[index] = useArr[i];
        result++;
    }
    cout << result;
    return 0;
}