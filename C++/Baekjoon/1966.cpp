// 1966. 프린터 큐 - 풀이 중,,,
#include <iostream>
#include <queue>
using namespace std;
// solution
// 1. queue로 풀이 + count 배열 만들어서
// 해당 값 이상인 count 배열 존재시 뒤로 push
// 2. hash table로 풀이
int main(){
    freopen("input.txt", "r", stdin);
    // 테스트 케이스 주어짐
    int testCase;
    cin >> testCase;
    for (int t=0; t<testCase; t++){
        int N;
        // 문서의 개수 N
        cin >> N;
        // 몇 번째로 인쇄 되었는 지 궁금한 문서의 인덱스 M
        int M;
        cin >> M;
        queue<int> q;
        int cnt[10] = {};

        // q에 문서 삽입 & cnt 배열 추가
        for (int i=0; i<N; i++){
            int num;
            cin >> num;
            
            q.push(num);
            cnt[num]++;
        }

        // cnt 배열 확인 후 q 회전
        // 궁금한 문서의 인덱스를 포인터로 생각해서 계속 증감 확인
        int p;
        p = M;
        while (p != -1){
            // 맨 앞 원소 확인
            int first = 0;
            first = q.front();
            // cnt 배열에서 해당 원소 이후 값들의 존재 확인
            bool exist = false;
            for (int i=first+1; i<10; i++){
                // cnt 배열이 존재할 경우 break
                if (cnt[i]){
                    exist = true;
                    break;
                }
            }
            // 있을 경우 -> 뒤로 보내기
            // 없을 경우 -> pop
            int cnt=0;
            if (exist){
                if (p == 0){
                    p = q.size() - 1;
                }
                // 뒤로 보내기,,
                q.push(q.front());
                q.pop();
            }
            else {
                if (p == 0){
                    p = -1;
                    continue;
                }
                q.pop();
                cnt++;
            }
            
        }
        cout << cnt << endl;
        
    }
}