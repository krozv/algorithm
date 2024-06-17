# 3665. 최종 순위
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

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

        # 처음 시작할 때 진입 차수가 0인 노드를 큐에 삽입
        for i in range(1, n + 1):
            if degree[i] == 0:
                q.append(i)

        # 위상 정렬 수행
        while q:
            if len(q) > 1:
                # 큐의 길이가 1보다 크면 여러 가지 가능한 순서가 있는 것이므로 특정할 수 없음
                return "?"

            current = q.popleft()
            result.append(current)

            for next_node in graph[current]:
                degree[next_node] -= 1
                if degree[next_node] == 0:
                    q.append(next_node)

        if len(result) == n:
            return " ".join(map(str, result))
        else:
            return "IMPOSSIBLE"

    print(topological_sorting())