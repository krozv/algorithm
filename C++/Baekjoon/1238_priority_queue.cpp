// 1238. 파티
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

#define MAX_N 1000
#define INF (int)1e9

using namespace std;

vector<pair<int, int>> graph[MAX_N+1];
vector<pair<int, int>> reverse_graph[MAX_N+1];

int dist[MAX_N+1];
bool visited[MAX_N+1];

void dijkstra(int start, int n, vector<pair<int, int>> graph[], int dist[]){
    // 초기화
    fill(dist, dist + n + 1, INF);
    fill(visited, visited + n + 1, false);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    dist[start] = 0;
    pq.push({0, start});

     while (!pq.empty()) {
        int current = pq.top().second;
        pq.pop();

        if (visited[current]) continue;
        visited[current] = true;

        for (auto &edge : graph[current]) {
            int next = edge.first;
            int weight = edge.second;

            if (dist[next] > dist[current] + weight) {
                dist[next] = dist[current] + weight;
                pq.push({dist[next], next});
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

    for (int i=1; i<=m; i++){
        int a, b, c;
        cin >> a >> b >> c;
        // a에서 b까지 가는데 c만큼의 시간이 걸림
        graph[a].push_back({b, c});
        reverse_graph[b].push_back({a, c});
    }
    
    int dist_to[MAX_N + 1];
    int dist_from[MAX_N + 1];
    int max_time = 0;

    dijkstra(x, n, graph, dist_to);

    dijkstra(x, n, reverse_graph, dist_from);

    for (int i = 1; i <= n; i++) {
        if (i == x) continue;
        if (dist_to[i] != (int)1e9 && dist_from[i] != (int)1e9) {
            max_time = max(max_time, dist_to[i] + dist_from[i]);
        }
    }
    
    cout << max_time << endl;

    return 0;
}