// 1018. 체스판 다시 칠하기
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int main(){
    freopen("input.txt", "r", stdin);
    int n, m;
    cin >> n >> m;
    int arr[50][50];
    for (int i=0; i<n; i++){
        string str;
        cin >> str;
        for (int j=0; j<m; j++){
            if (str[j] == 'W'){
                arr[i][j] = 0;
            }
            else {
                arr[i][j] = 1;
            }
        }
    }
    int cnt=64;
    for (int i=0; i<n-7; i++){
        for (int j=0; j<m-7; j++){
            // 시작을 0으로 가정
            int temp = 1;
            int countFromZero = 0;
            for (int k=0; k<8; k++){
                temp = 1- temp;
                for (int l=0; l<8; l++){
                    if (temp == arr[i+k][j+l]){
                        countFromZero++;
                    }
                    temp = 1 - temp;
                }
            }
            // 시작을 1로 가정
            temp = 0;
            int countFromOne = 0;
            for (int k=0; k<8; k++){
                temp = 1 - temp;
                for (int l=0; l<8; l++){
                    if (temp == arr[i+k][j+l]){
                        countFromOne++;
                    }
                    temp = 1 - temp;
                }
            }
            // cout << "countFromZero: " << countFromZero << endl;
            // cout << "countFromOne: " << countFromOne << endl;

            if (countFromOne > countFromZero){
                cnt = min(cnt, countFromZero);
                // cout << "zero" << endl;
            }
            else {
                cnt = min(cnt, countFromOne);
                // cout << "one" << endl;
            }

        }
    }
    cout << cnt;
    // 입력을 W -> 0, B -> 1로 바꿔서 배열에 받을 것
    // 완전탐색으로 개수를 셀 예정
    // 1과 0을 시작으로 가정한 두 케이스에 대해서 cnt 개수 세서 최소값 도출하기

}