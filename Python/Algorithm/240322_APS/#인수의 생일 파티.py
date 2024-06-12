import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
def bfs(start, adj):
    visited = [0] * (N + 1)
    visited[start] = 0
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for to, weight in adj[now]:
            if to != start:
                if not visited[to] or visited[to] > visited[now] + weight:
                    visited[to] = visited[now] + weight
                    q.append(to)
    return visited


T = int(input())
for t in range(1, T+1):
    N, M, X = map(int, input().split())
    adj1 = [[] for _ in range(N+1)]
    adj2 = [[] for _ in range(N+1)]
    ans = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        adj1[s].append([e, w])
        adj2[e].append([s, w])

    visited1 = bfs(X, adj1)
    visited2 = bfs(X, adj2)
    for i in range(N+1):
        ans[i] = visited1[i] + visited2[i]
    print(f'#{t} {max(ans)}')




