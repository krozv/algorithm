// 1654. 랜선 자르기
#include <iostream>
#include <algorithm>
// K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없음
// 정수만큼 자름
// N개보다 많이 만드는 것도 N개를 만드는 것에 포함
// 최대 랜선의 길이를 구하는 프로그램
using namespace std;
int main(){
    freopen("input.txt", "r", stdin);
    // 가지고 있는 랜선의 개수 K
    int K;
    cin >> K;
    // 필요한 랜선의 개수 N
    int N;
    cin >> N;
    // K줄에 걸쳐 가지고 있는 각 랜선의 길이가 정수로 입력된다
    int arr[10000];
    int right = 0;
    for (int i=0; i<K; i++){
        cin >> arr[i];
        right = max(right, arr[i]);
    }

    long long left = 1;
    long long target;
    long long result;
    while (left <= right){
        // target 선정
        target = (left + right) / 2;

        // 가능, 불가능 판단
        int cnt=0;
        for (int i=0; i<K; i++){
            cnt += arr[i] / target;
        }
        if (cnt >= N){
            result = target;
            left = target + 1;
        }
        else {
            right = target - 1;
        }
    }
    cout << result;
}