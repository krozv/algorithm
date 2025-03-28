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
    // 그 사람을 기준으로 덩치가 큰 사람을 골라야 하므로
    // 그냥 완전 탐색하는게 나을지도
    int arr[50][3] = {};
    for (int i=0; i<N; i++){
        cin >> arr[i][0] >> arr[i][1];
    }
    // 완전탐색
    for (int i=0; i<N; i++){
        for (int j=i+1; j<N; j++){
            // 덩치 비교
            if (arr[i][0] > arr[j][0] && arr[i][1] > arr[j][1]){
                arr[j][2]++;
            }
            else if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]){
                arr[i][2]++;
            }
        }
    }

    for (int i=0; i<N; i++){
        cout << arr[i][2]+1 << ' ';
    }
}