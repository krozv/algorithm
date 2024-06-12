# 2252. 줄 세우기
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for node in range(1, N+1):
    if indegree[node] == 0:
        q.append(node)

result = []
while q:
    now = q.popleft()
    result.append(now)
    for to in graph[now]:
        indegree[to] -= 1
        if indegree[to] == 0:
            q.append(to)

for i in result:
    print(i, end=" ")