//단어수학
#include <bits/stdc++.h>
using namespace std;

int N, i;
char words[11][11];
int numbers[11][11] = {-1,};

int WordCount(char cmpWord, int row){
    int cnt = 12;
    for(int i = 0; i < 11; ++i)
        if(cmpWord == words[row][i]) return cnt = i;
    return cnt;
}

void WordtoNum(char word, int num){
    for(int i = 0; i < N; ++i){
        int j = 0;
        while(true){
            if(words[i][j] == '\0') break;
            if(words[i][j] == word) numbers[i][j] = num;
            j++;   
        }
    }
}



int main(){
    cin >> N;

    for(int i = 0; i < N; ++i){
        cin >> words[i];
    }

    for(int i = 0; i < 10; ++i){
        int num = 9;
        char word = '\0'; int nextCol = 0;
        for(int j = 0; j < N; ++j){
            if(words[j][i] != '\0'){
                if(word != '\0') word = words[j][i];
                else{
                    int cmpCount = WordCount(words[j][i],j);
                   if(nextCol > cmpCount){
                       nextCol = cmpCount;
                       word = words[j][i];
                   }
                }
            }
            break;
        }
        WordtoNum(word,num--);
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < 11; j++)
            cout << numbers[i][j];
        cout << '\n';
    }


    return 0;
}