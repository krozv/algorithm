#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;

const int MAX_N = 1000; // 도시 최대 개수

struct Edge {
    int dest;
    int w;
    Edge(int d, int weight) : dest(d), w(weight) {}
};

vector<Edge> graph[MAX_N];

// 초기화 함수
void init(int N, int K, int sCity[], int eCity[], int mLimit[]) {
    for (int i = 0; i < N; i++) {
        graph[i].clear();
    }
    for (int i = 0; i < K; i++) {
        graph[sCity[i]].push_back(Edge(eCity[i], mLimit[i]));
    }
}
// 추가해
void add(int sCity, int eCity, int mLimit) {
    graph[sCity].push_back(Edge(eCity, mLimit));
}

// 우선순위큐 사용해서 다익스트라?
int calculate(int sCity, int eCity) {
    vector<int> maxWeight(MAX_N, 0);
    priority_queue<pair<int, int> > pq;
    pq.push(make_pair(INT_MAX, sCity));
    
    while (!pq.empty()) {
        // 큐에서 꺼냄
        int weight = pq.top().first;
        int current = pq.top().second;
        pq.pop();
        
        // 도착도시면 리턴
        if (current == eCity) {
            return weight;
        }
        
        // 최대 중량 계산
        for (int i=0; i < graph[current].size(); i++) {
            
        }

    }
    
    return -1; // 불가능하면
}

// 실행

#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h> 

extern void init(int N, int K, int sCity[], int eCity[], int mLimit[]);
extern void add(int sCity, int eCity, int mLimit);
extern int calculate(int sCity, int eCity);

#define MAX_E 4000
#define CMD_INIT 100
#define CMD_ADD 200
#define CMD_CALC 300

static bool run() {
    int q;
    scanf("%d", &q);

    int n, k;
    int sCityArr[MAX_E], eCityArr[MAX_E], mLimitArr[MAX_E];
    int sCity, eCity, mLimit;
    int cmd, ans, ret = 0;
    bool okay = false;

    for (int i = 0; i < q; ++i) {
        scanf("%d", &cmd);
        switch (cmd) {
            case CMD_INIT:
                okay = true;
                scanf("%d %d", &n, &k);
                for (int j = 0; j < k; ++j) {
                    scanf("%d %d %d", &sCityArr[j], &eCityArr[j], &mLimitArr[j]);
                }
                init(n, k, sCityArr, eCityArr, mLimitArr);
                break;
            case CMD_ADD:
                scanf("%d %d %d", &sCity, &eCity, &mLimit);
                add(sCity, eCity, mLimit);
                break;
            case CMD_CALC:
                scanf("%d %d %d", &sCity, &eCity, &ans);
                ret = calculate(sCity, eCity);
                if (ans != ret)
                    okay = false;
                break;
            default:
                okay = false;
                break;
        }
    }
    return okay;
}

int main() {
    setbuf(stdout, NULL);
    freopen("sample_input.txt", "r", stdin);

    int T, MARK;
    scanf("%d %d", &T, &MARK);

    for (int tc = 1; tc <= T; tc++) {
        int score = run() ? MARK : 0;
        printf("#%d %d\n", tc, score);
    }

    return 0;
}
