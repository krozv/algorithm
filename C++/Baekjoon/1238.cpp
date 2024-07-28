// 1238. 파티
#include <iostream>
#include <algorithm>
#include <cstring>

#define MAX_N 1000
using namespace std;
int graph[MAX_N+1][MAX_N+1];
int dist[MAX_N+1];
bool visited[MAX_N+1];

void dijkstra(int start, int n){
    // 초기화
    fill(dist, dist + n + 1, (int)1e9);
    fill(visited, visited + n + 1, false);
    dist[start] = 0;

    for (int i=1; i<=n ;i++){
        int min_dist = (int)1e9;
        int min_index = -1;

        // 최소 거리 정점 찾기
        for (int j=1; j<=n; j++){
            if (visited[j])
                continue;
            if (dist[j] < min_dist) {
                min_dist = dist[j];
                min_index = j;
            }
        }
        if (min_index == -1) break;
        visited[min_index] = true;

        for (int j = 1; j <= n; j++) {
            if (graph[min_index][j] != 0 && dist[j] > dist[min_index] + graph[min_index][j]) {
                dist[j] = dist[min_index] + graph[min_index][j];
            }
        }
    }
}
int main(){
    freopen("input.txt", "r", stdin);
    // n개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있음
    // x번 마을에 모임 == 도착지
    // m 개의 단방향 도로 == edge
    // 가장 많은 시간소비하는 학생?
    int n, m ,x;
    cin >> n >> m >> x;

    // graph 초기화
    memset(graph, 0, sizeof(graph)); 

    for (int i=1; i<=m; i++){
        int a, b, c;
        cin >> a >> b >> c;
        // a에서 b까지 가는데 c만큼의 시간이 걸림
        graph[a][b] = c;
    }
    
    int dist_to[MAX_N + 1];
    int dist_from[MAX_N + 1];
    int max_time = 0;

    dijkstra(x, n);
    memcpy(dist_to, dist, sizeof(dist)); // 복사

    for (int i = 1; i <= n; i++) {
        if (i == x) continue;
        dijkstra(i, n);
        dist_from[i] = dist[x];
    }

    for (int i = 1; i <= n; i++) {
        if (i == x) continue;
        if (dist_to[i] != (int)1e9 && dist_from[i] != (int)1e9) {
            max_time = max(max_time, dist_to[i] + dist_from[i]);
        }
    }
    
    cout << max_time << endl;

    return 0;
}