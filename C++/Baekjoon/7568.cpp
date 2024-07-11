// 7568. 덩치
// (x, y), (p, q)
// x > p && y > q: e더 크다
// 반복 가능
// x > p && y < q: 덩치를 판단할 수 없음 같은 등수로 표시
// 학생 N명의 몸무게와 키가 담긴 입력을 읽어서 각 사람의 등수를 계산하여 출력
// 휴.. 다시 읽고 풀어야함

#include <iostream>
using namespace std;
int main(){
    freopen("input.txt", "r", stdin);
    // 전체 사람의 수 N
    // 2 <= N <= 50
    int N;
    cin >> N;
    // N개의 줄에 각 사람의 몸무게와 키 x, y
    // 10 <= x, y <= 200
    // 완전 탐색 시 nlogn 예상
    int w[201]={};
    int h[201]={};
    int arr[50][3] = {};

    // array에 값 저장 및 확인
    for (int i=0; i<N; i++){
        int weight, height;
        cin >> weight >> height;
        arr[i][0] = weight;
        arr[i][1] = height;
        w[weight] = 1;
        h[height] = 1;
    }

    // 누적합 계산
    for (int i=1; i<201; i++){
        w[i] = w[i] + w[i-1];
        h[i] = h[i] + h[i-1];
    }
    // 누적합 확인 코드
    // for (int i=0; i<201; i++){
    //     cout << i << ": " << w[i] << endl;
    // }
    // arr 배열 등수로 변경
    for (int i=0; i<N; i++){
        arr[i][0] = w[arr[i][0]];
        arr[i][1] = h[arr[i][1]];
        // cout << i << ' ' << arr[i][0] << ' ' << arr[i][1] << endl;
        arr[i][2] = arr[i][0] + arr[i][1];
    }
    // 등수의 합 배열 다시 센다...
    int cnt[102] = {};
    for (int i=0; i<N; i++){
        cnt[arr[i][2]]++;
    }
    // 합 한번더 확인한다
    for (int i=0; i<101; i++){
        if (cnt[i]){
            // cout << i << ": " << cnt[i] << endl;
        }
    }
    for (int i=100; i>0; i--){
        cnt[i-1] = cnt[i-1] + cnt[i];
    }
    cout << endl;
    // 누적합 잘 되었는 지 확인
    for (int i=100; i>0; i--){
        if (cnt[i]){
            // cout << i << ": " << cnt[i] << endl;
        }
    }
    // 등수로 변환
    for (int i=0; i<N; i++){
        // cout << arr[i][2] << endl;
        cout << cnt[arr[i][2]+1]+1 << ' ';
        // cout << endl;
    }
}