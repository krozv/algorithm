# 1766. 문제집
import sys
sys.stdin = open('../../Algorithm/TopologicalSorting/input.txt', 'r')
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
    if not degree[i]:
        q.put(i)

result = []

while q.qsize():
    now = q.get()
    result.append(now)
    for to in graph[now]:
        degree[to] -= 1
        if not degree[to]:
            q.put(to)

for node in result:
    print(node, end=" ")