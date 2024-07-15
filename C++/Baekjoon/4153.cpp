#include <iostream>
using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    bool flag = true;
    while (true){
        int a, b, c;
        cin >> a >> b >> c;
        if (a == 0 && b ==0 && c == 0){
            break;
        }
        // 순서 정렬
        int sm = 0, md = 0, lg = 0;
        if (a <= b && a <= c){
            sm = a;
            if (b <= c){
                md = b;
                lg = c;
            } else {
                md = c;
                lg = b;
            }
        }
        else if (b <= a && b <= c){
            sm = b;
            if (a <= c){
                md = a;
                lg = c;
            } else {
                md = c;
                lg = a;
            }
        }
        else {
            sm = c;
            if (a <= b){
                md = a;
                lg = b;
            } else {
                md = b;
                lg = a;
            }
        }
        if (sm * sm + md * md == lg * lg){
            cout << "right" << endl;
        } else {
            cout << "wrong" << endl;
        }
        
    }
}