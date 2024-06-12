# 창용 마을 무리의 개수
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for to in graph[now]:
            if not visited[to]:
                q.append(to)
                visited[to] = 1


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            bfs(i)
            cnt += 1
    print(f'#{t} {cnt}')