// 18110. solved.ac
// problem
// 의견이 없을 경우 난이도 = 0
// 의견이 하나 이상 있으면, 모든 사람의 난이도 의견의 30% 절사평균

// 절사평균
// 가장 큰값, 가장 작은값들 제외하고 평균
// 위에서 %만큼 제외
// 제외되는 사람의 수: 위, 아래에서 각각 반올림

// 마지막으로 계산된 평균도 반올림

#include <iostream>
#include <cmath>
using namespace std;
int main() {
    freopen("input.txt", "r", stdin);
    // 난이도 의견 개수
    // 0 <= n <= 3e5
    int n;
    cin >> n;

    if (n == 0){
        cout << 0;
    }
    else{
    // cnt에 저장하고 값을 뺀 후 sum 구하는 식으로 접근
    int cnt[31] = {};

    // 난이도 의견 n개 주어짐
    // 1 <= 난이도 <= 30;
    for (int i=0; i<n; i++){
        int num;
        cin >> num;
        cnt[num]++;
    }
    // 30% 절사평균이므로 계산 반영안하는 명 수 구함
    int exclude_count = 0;
    exclude_count = round(n * 0.15);

    // 아래에서 절삭
    int down = exclude_count;
    for (int i=1; i<=30; i++){
        if (!down)
            break;
        while (cnt[i]){
            cnt[i]--;
            down--;
            if (!down)
                break;
        }
    }
    // 위에서 절삭
    int up = exclude_count;
    for (int i=30; i>0; i--){
        if (!up)
            break;
        while (cnt[i]){
            cnt[i]--;
            up--;
            if (!up)
                break;
        }
    }
    // 합 구하기
    int sum_val = 0;
    for (int i=1; i<=30; i++){
        if (cnt[i]){
            sum_val += i * cnt[i];
        }
    }
    cout << round(double(sum_val) / (n-exclude_count*2));
    }
}