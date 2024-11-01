// 1003.피보나치 함수
#include <iostream>
using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    // testcase T
    int T;
    cin >> T;
    for (int i=0; i<T; i++){
        // N이 주어진다
        int N;
        cin >> N;
        
        int arr[41][2] = {};
        arr[0][0] = 1;
        arr[1][1] = 1;
        for (int j=2; j<=N; j++){
            for (int k=0; k<2; k++){
                arr[j][k] = arr[j-1][k] + arr[j-2][k];
            }
        }

        cout << arr[N][0] << ' ' << arr[N][1] << endl;
        
    }
}