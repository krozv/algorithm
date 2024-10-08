// 1436. 영화감독 숌
// 666이 들어간 수
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main() {
    // N을 입력받음
    // 1 <= N < 10,000
    int N;
    cin >> N;
    // 1. 완전탐색
    // 1부터 조건이 만족할 때까지 숫자를 세고, 조건 만족 후 조건문 종료
    bool satisfied = false;
    int i = 1;
    int order = 0;
    while (!satisfied){
        string str = to_string(i);
        // 6개수 센다
        int cnt = 0;
        for (int j=0; j<str.length(); j++){
            if (str[j] == '6'){
                cnt++;
            }
            else {
                cnt = 0;
            }
            if (cnt == 3){
                order++;
                break;
            }
        }
        if (N == order){
            satisfied = true;
            break;
        }
        i++;
    }
    cout << i;
}