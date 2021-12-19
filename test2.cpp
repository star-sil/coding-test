#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
bool compare(int a, int b){
    return a < b;
}

int main()
{
    int T;
    cin >> T;
    // char NumT = {"1","2","3"};
    // char ColorT = {"R","G","P"};
    // char ShapeT = {"E","D","T"};
    // char UmT = {"F","S","W"};

    int result[T];
    for(int i =0; i < T; i++)
    {
        int NumT[3] = {0,};
        int ColorT[3] = {0,};
        int ShapeT[3] = {0,};
        int UmT[3] = {0,};
        result[i] = 0;
        int N;
        cin >> N;
        char Num[N]; char Shape[N]; char Color[N]; char Um[N];
        for(int i = 0; i < N; i++)
        {
            string str;
            cin >> str;
            //Num[i] = str[0]; Color[i] = str[1]; Shape[i] = str[2]; Um[i] = str[3];
            switch(str[0])
            {
                case '1':
                    NumT[0] += 1;
                    break;
                case '2':
                    NumT[1] += 1;
                    break;
                case '3':
                    NumT[2] += 1;
                    break;
            }
            switch(str[1])
            {
                case 'R':
                    ColorT[0] += 1;
                    break;
                case 'G':
                    ColorT[1] += 1;
                    break;
                case 'B':
                    ColorT[2] += 1;
                    break;
            }
            switch(str[2])
            {
                case 'E':
                    ShapeT[0] += 1;
                    break;
                case 'D':
                    ShapeT[1] += 1;
                    break;
                case 'T':
                    ShapeT[2] += 1;
                    break;
            }
            switch(str[3])
            {
                case 'F':
                    UmT[0] += 1;
                    break;
                case 'S':
                    UmT[1] += 1;
                    break;
                case 'W':
                    UmT[2] += 1;
                    break;
            }
        }
        for (int i = 0; i < 4; i++)
        {
            sort(NumT, NumT+3,compare);
            sort(ColorT, ColorT+3,compare);
            sort(ShapeT, ShapeT+3,compare);
            sort(UmT, UmT+3,compare);
        }
        int nNum = NumT[0] / 3 + NumT[1] / 3 + NumT[2] / 3;
        int nColor = ColorT[0] / 3 + ColorT[1] / 3 + ColorT[2] / 3;
        int nShape = ShapeT[0] / 3 + ShapeT[1] / 3 + ShapeT[2] / 3;
        int nUm = UmT[0] / 3 + UmT[1] / 3 + UmT[2] / 3;
        if(result[i] < nNum)
        {
            result[i] = nNum;
        }
        if(result[i] < nColor)
        {
            result[i] = nColor;
        }
        if(result[i] < nShape)
        {
            result[i] = nShape;
        }
        if(result[i] < nUm)
        {
            result[i] = nUm;
        }

    }
    for(int i = 0; i < T; i ++)
    {
        cout << i+1 << "#" << " " << result[i] << "\n";
    }
}