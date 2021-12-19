#include <iostream>
#include <algorithm>
using namespace std;

bool compare(int a, int b)
{
    return a < b;
}

int main(){
    int T, N;
    cin >> T;

    int result[T];
    for(int i = 0; i < T; i++)
    {
        result[i] = 0;
        cin >> N;
        int arr[N];
        for(int j = 0; j < N; j++)
        {
            cin >> arr[j];
        }
        sort(arr, arr + N,compare);
        int arr2[N];
        for(int j = 0; j < N ; j++)
        {
            arr2[j] = 0;
        }
        for(int j = N-1; j >= 0; j--)
        {
            //cout << arr2[j] << " ==" << arr[j] << "\n";
            if(arr2[j] == 1)
            {
                continue;
            }
            for(int k = 0; k < N; k++)
            {
                //cout << i << ':' << arr[k] << " " << arr[j] << "\n";
                if(arr2[k] == 1 || j == k)
                {
                    continue;
                }
                //cout << "1: "<< arr2[k] << " " << arr2[j] << "\n";
                if((arr[k] + arr[j]) % 2 == 0)
                {
                    cout << i << ':' << arr[k] << " " << arr[j] << "\n";
                    result[i] += arr[j];
                    arr2[k] = 1; arr2[j] = 1;
                    break;
                }
                //cout <<"2: " << arr2[k] << " " << arr2[j] << "\n";     
            }
        }
        for(int j = N -1; j >= 0; j--)
        {
            if(arr2[j] == 1)
            {
                continue;
            }
            for(int k = 0; k < N; k++)
            {
                if(arr2[k] == 1)
                {
                    continue;
                }
                else
                {
                    arr2[j] = 1; arr2[k] = 1;
                    result[i] += arr[k];
                    break;
                }
            }
        }
    }
    for(int i = 0; i < T; i++){
        cout << "#" << i+1 << " " << result[i] << '\n';
    }
}