// 10773. 제로
// 스택으로 풀면 될듯
#include <iostream>
#include <stack>
using namespace std;
int main(){
    freopen("input.txt", "r", stdin);
    // 정수 K 주어짐
    int K;
    cin >> K;
    // 정수 n이 K번 주어짐
    // 0 <= n <= 1,000,000
    stack<int> stk;
    for (int i=0; i<K; i++){
        int n;
        cin >> n;
        // stack pop
        if (n == 0){
            stk.pop();
        }
        // stack push
        else {
            stk.push(n);
        }
    }
    if (stk.empty()){
        cout << 0;
    } 
    else {
        // stk 합 구하기
        int sum_val = 0;
        while (!stk.empty()){
            int x = stk.top();
            sum_val += x;
            stk.pop();
        }
        cout << sum_val;
    }
}