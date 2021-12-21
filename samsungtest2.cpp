#include <iostream>
using namespace std;


//가능 하면 이동시간 반환 안되면 -1 반환
int check_possible(int arr[], int Dmax, int start,int *count)
{
    int dis = Dmax - start;
    int tmpCount = *count;
    int tmp = 0;
    int step,end;
    while(1)
    {
        step = start+1;
        end = step + 5;
        if(end >= Dmax)
        {
            *count = tmpCount  + tmp;
            return 1;
        }
        for(int i = step; i <= end; i++)
        {
            if(arr[i] == 2)
            {
                //cout << "check1 " << arr[i] << " " <<  i <<  " " << tmp<<"\n";
                start = i;
                continue;
            }
        }
        if(start+1 == step)
        {
            //cout << "check2\n";
            return 0;
        }
        tmp += 1;
        if(dis + tmp > 15)
        {
            return 0;
        }
    }
    *count = tmpCount + tmp;
    return 1;
}

int main()
{
    int T;
    cin >> T;
    
    int timearr[T];
    for(int i = 0; i < T; i++)
    {
        int N;
        cin >> N;
        int Count = 0;
        int Dmax = 15;
        int arr[N];
        for(int j = 0; j < N; j++)
        {
            cin >> arr[j];
        }

        int start = 0;
        int flag = 1;
        while(flag == 1)
        {
            if(Dmax >= N)
            {
                Dmax = N-1;
            }
            //cout << i << " " << Dmax << " " << start << "\n";
            for(int j = Dmax; j >= start; j--)
            {
                if(j == start)
                {
                    flag = 0;
                    break;
                }
                cout << "1 "<< start << " " << j << "\n";
                if(arr[j] == 3)
                {
                    cout <<"2 "<< start << " " << j << "\n";
                    //성공
                    if(check_possible(arr,j,start,&Count) != 0)
                    {
                        start = j;
                        Dmax = j + 15;                        
                        cout <<"3 "<< start << " " << Dmax << " "<< Count<<  "\n";
                        break;                        
                    }
                    else
                    {
                        continue;
                    }
                }
            }
        }
        timearr[i] = (start + Count) > 0 ? start + Count : -1;
    }
    for(int i = 0; i < T; i++)
    {
        cout << "#" << i+1 << " " << timearr[i] << "\n";
    }
}