// 17219. 비밀번호 찾기
// 메모장에서 비밀번호를 찾는 프로그램 만들기
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;
int main() {
    freopen("input.txt", "r", stdin);
    // 저장된 사이트의 주소 수 N
    // 1 <= N <= 100,000
    int N;
    cin >> N;

    // 비밀번호 찾으려는 사이트 주소의 수 M
    // 1 <= M <= 100,000
    int M;
    cin >> M;

    // N개의 줄: 사이트 주소 + 비밀번호
    unordered_map<string, string> m;
    m.reserve(N);

    for (int i=0; i<N; i++){
        string url, pw;
        cin >> url >> pw;
        m[url] = pw;
    }

    // N+2번째 줄부터 M개의 줄: 찾으려는 사이트 주소
    // 반드시 이미 저장된 사이트 주소가 입력됨
    for (int i=0; i<M; i++){
        string target_url;
        cin >> target_url;
        cout << m[target_url] << endl;
    }
}