// 5972. 택배 배송
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

#define MAX_N 50000
#define INF (int)1e9

using namespace std;

vector<pair<int, int>> graph[MAX_N+1];

int dist[MAX_N+1];
bool visited[MAX_N+1];

void dijkstra(int start, int n, vector<pair<int, int>> graph[], int dist[]){
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

        // 현재 정점 current와 연결된 모든 인접 정점에 대해 반족
        for (auto &edge : graph[current]) {
            int next = edge.first;
            int weight = edge.second;
            // cout << "test";
            if (dist[next] > dist[current] + weight) {
                dist[next] = dist[current] + weight;
                pq.push({dist[next], next});
            }
        }
    }
}
int main() {
    freopen("input.txt", "r", stdin);
    int n, m;
    cin >> n >> m;

    for (int i=1; i<=m; i++){
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }

    int min_val = INF;
    dijkstra(1, n, graph, dist);

    // for (int i=2; i<=n; i++){
    //     if (dist[i] != INF){
    //         min_val = min(min_val, dist[i]);
    //     }
    // }
    cout << dist[n] << endl;
}