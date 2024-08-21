// 2920. 음계
#include <iostream>
using namespace std;
int main() {
    int arr[8] = {};
    for (int i=0; i<8; i++){
        cin >> arr[i];
    }
    int state = 1;
    if (arr[0] == 1){
        int cnt=1;
        for (int i=0; i<8; i++){
            if (arr[i] == cnt){
                cnt++;
                continue;
            }
            state = 0;
            break;
        }
        if (state)
            state = 1;
    } else if (arr[0] == 8) {
        int cnt = 8;
        for (int i=0; i<8; i++){
            if (arr[i] == cnt){
                cnt--;
                continue;
            }
            state = 0;
            break;
        }
        if (state)
            state = -1;
    } else {
        state = 0;
    }
    if (state == 1)
        cout << "ascending";
    else if (state == -1)
        cout << "descending";
    else 
        cout << "mixed";
}