// 30802. 웰컴 키트
// 티셔츠: 남아도 돼. 부족 X
// 펜: 남아도 x, 부족 x
// T장, 몇 묶음
// P자루, 몇 묶음 or 한 자루

#include <iostream>
using namespace std;
int main(){
    freopen("input.txt", "r", stdin);
    // N
    int N;
    cin >> N;
    // S, M, L, XL, XXL, XXXL
    int arr[6] = {};
    for (int i=0; i<6; i++){
        cin >> arr[i];
    }
    int T, P;
    cin >> T >> P;
    int tshirt = 0;
    for (int i=0; i<6; i++){
        tshirt += arr[i]/T;
        if (arr[i]%T != 0){
            tshirt++;
        }
    }
    cout << tshirt << endl;
    cout << N / P << ' ' << N % P;
}