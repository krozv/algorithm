#include <iostream>
#include <string>
using namespace std;
int main(){
    int n;
    cin >> n;

    int cnt_2 = 0;
    int cnt_5 = 0;

    for (int i=1; i<=n; i++){
        
        int num = i;
        while (num % 2 == 0){
            num /= 2;
            cnt_2++;
        }
        while (num % 5 == 0){
            num /= 5;
            cnt_5++;
        }
    }

    if (cnt_2 >= cnt_5){
        cout << cnt_5;
    }
    else {
        cout << cnt_2;
    }

}