import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, length = map(int, input().split())
    graph[a].append((b, length))
    graph[b].append((a, length))

def bfs(s, e):
    q = deque()
    q.append((s, 0))
    visited = [0] * (n+1)
    visited[s] = 1
    while q:
        v, d = q.popleft()
        if v == e:
            return d

        for i, length in graph[v]:
            if not visited[i]:
                visited[i] = 1
                q.append((i, d+length))

for _ in range(m):
    n1, n2 = map(int, input().split())
    print(bfs(n1, n2))