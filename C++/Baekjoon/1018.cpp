// 1018. 체스판 다시 칠하기
#include <iostream>
#include <string>
using namespace std;
int main(){
    freopen("input.txt", "r", stdin);
    int n, m;
    cin >> n >> m;
    int arr[50][50];
    for (int i=0; i<n; i++){
        string str;
        getline(cin, str);
        for (int j=0; j<m; j++){
            if (str[j] == 'W'){
                arr[i][j] = 0;
            }
            else {
                arr[i][j] = 1;
            }
        }
    }
    for (int i=0; i<n; i++){
        for (int j=0;)
    }
    // 입력을 W -> 0, B -> 1로 바꿔서 배열에 받을 것
    // 완전탐색으로 개수를 셀 예정
    // 1과 0을 시작으로 가정한 두 케이스에 대해서 cnt 개수 세서 최소값 도출하기

}