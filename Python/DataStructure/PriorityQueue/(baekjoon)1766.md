# [baekjoon] 1766. 문제집

## Data Structure

- 유향 그래프 (directed graph)

## Algorithm

- 우선순위 큐

## How to solve

### Method

- 1~N번까지 총 N개의 문제로 되어 있는 문제집
- 문제는 난이도 순서로 출제. 클수록 어려운 문제
- 먼저 푸는 것이 좋은 문제가 있는 문제가 존재 = 문제 간 방향 존재
- 가능하면 쉬운 문제부터 풀어야함

### Constraint
1. 시간 복잡도
- 2초 : 2,000,000,000
2. 공간 복잡도

### Review
- topological sorting으로 풀려고 접근함
- 문제 번호가 가장 낮은 것부터 풀어야 하므로 반복문 사용함
- 시간초과
```python
# 1766. 문제집
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

q = deque()

for i in range(1, N+1):
    if not degree[i]:
        q.append(i)
        break

result = []
visited = [0] * (N+1)
while q:
    now = q.pop()
    result.append(now)
    visited[now] = 1
    for to in graph[now]:
        degree[to] -= 1
    for i in range(1, N+1):
        if not degree[i] and not visited[i]:
            q.append(i)
            break

for node in result:
    print(node, end=" ")
```
- heapq 사용하면 시간 감소 가능
- 우선순위 큐 라이브러리 사용함
- 메모리: 43764 KB
- 시간: 312 ms
```python
# 1766. 문제집
import sys
input = sys.stdin.readline
from queue import PriorityQueue

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

q = PriorityQueue()

for i in range(1, N+1):
    # 차수가 0인 노드들 우선순위 큐에 put
    if not degree[i]:
        q.put(i)

result = []

# queue의 크기가 0이 될때까지 반복
while q.qsize():    
    now = q.get()
    result.append(now)
    for to in graph[now]:
        degree[to] -= 1
        if not degree[to]:
            q.put(to)

for node in result:
    print(node, end=" ")
```