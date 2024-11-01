import sys
input = sys.stdin.readline
tc = int(input())

def bellman_ford(n, edges, start, visited):
    dist = [1e9] * (n + 1)
    dist[start] = 0
    visited[start] = True

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != 1e9 and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                visited[v] = True

    for u, v, w in edges:
        if dist[u] != 1e9 and dist[u] + w < dist[v]:
            return True  # 음수 사이클 존재

    return False

for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    has_negative_cycle = False
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:  # 아직 방문하지 않은 노드에서만 시작
            if bellman_ford(n, edges, i, visited):
                has_negative_cycle = True
                break

    if has_negative_cycle:
        print("YES")
    else:
        print("NO")
