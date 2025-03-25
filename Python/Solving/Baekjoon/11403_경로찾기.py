# 11403. 경로 찾기
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
checked = [[0] * N for _ in range(N)]
adj = [[] for _ in range(N)]

def func(s, curr):
    for node in adj[curr]:
        if not visited[s][node]:
            visited[s][node] = 1
            func(s, node)

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            adj[i].append(j)

start = 0
visited = [[0] * N for _ in range(N)]

for i in range(N):
    func(i, i)

for row in visited:
    print(" ".join(list(map(str, row))))
