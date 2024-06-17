# [baekjoon] 3665. 최종 순위

## Data Structure

- 유향 그래프 (directed graph)

## Algorithm

- topological sorting

## How to solve

### Method
- 테스트 케이스 개수(t)가 주어짐
- 팀의 수(n)이 주어짐
- 유향 그래프 정보가 주어짐
- 바뀐 노드의 수(m)이 주어짐
- 바뀐 노드의 정보에 따라 유향 그래프를 변경함
- [참고](https://hongcoding.tistory.com/96)
- **노드 간 모든 간선을 표시해야함**

### Constraint
1. 시간 복잡도
    - O((n+E) * t)
    - test case (t): 1 <= t <= 100
    - 2 <= n <= 500
    - E = n-1
    - 1초 : 1,000,000,000
2. 공간 복잡도

### Review
- 위상정렬 없이 문제를 해결할 수 있다고 생각함
- 차수가 모든 노드가 다를 것이기 때문에, 차수가 작은 팀 순으로 정렬하여 출력하면 되지 않을까라고 생각함
- 하지만 에러
```python
# 3665. 최종 순위
import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    n = int(input()) # 팀의 수
    team = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    degree = [0] * (n+1)

    # graph로 변경
    for i in range(n):
        for j in range(i+1, n):
            graph[team[i]].append(team[j])
            degree[team[j]] += 1

    m = int(input())    # 변경된 순위

    def change_graph():
        flag = True
        for _ in range(m):
            a, b = map(int, input().split())
            if a in graph[b]:
                graph[b].remove(a)
                degree[a] -= 1
                graph[a].append(b)
                degree[b] += 1
            elif b in graph[a]:
                graph[a].remove(b)
                degree[b] -= 1
                graph[b].append(a)
                degree[a] += 1
            else:
                flag = False
        if flag:
            result = sorted(range(len(degree)), key=lambda x: degree[x])
            for k in range(1, n+1):
                print(result[k], end=" ")
            print()
        else:
            print("IMPOSSIBLE")

    change_graph()
```
- 위상정렬로 풀었을 경우 통과함
- 위 코드와 차이를 모르겠음
- 메모리: 34112 KB, 시간: 760 ms
```python
# 3665. 최종 순위
import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for t in range(1, T+1):
    n = int(input()) # 팀의 수
    team = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    degree = [0] * (n+1)

    # graph 변경
    for i in range(n):
        for j in range(i+1, n):
            graph[team[i]].append(team[j])
            degree[team[j]] += 1

    m = int(input())    # 변경된 순위
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[b].remove(a)
            degree[a] -= 1
            graph[a].append(b)
            degree[b] += 1
        else:
            graph[a].remove(b)
            degree[b] -= 1
            graph[b].append(a)
            degree[a] += 1

    def topological_sorting():
        q = deque()
        result = []

        for i in range(1, n+1):
            if not degree[i]:
                q.append(i)

        while q:
            if len(q) > 1:
                return "?"

            now = q.popleft()
            result.append(now)

            for to in graph[now]:
                degree[to] -= 1
                if degree[to] == 0:
                    q.append(to)

        if len(result) == n:
            return " ".join(map(str, result))
        else:
            return "IMPOSSIBLE"

    print(topological_sorting())
```