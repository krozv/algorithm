# 16236. 아기 상어
"""
작은 물고기는 먹고
같은 물고기는 pass
큰 물고기는 못감
이동 1초
이동과 동시에 물고기를 먹음 -> 먹으면 빈 칸

먹을 수 있는 물고기 없으면 -> 엄마!!!!
먹을 수 있는 물고기 1 -> 그거 먹음
먹을 수 있는 물고기 1 초과 -> 가장 가까운 물고기
거리의 최솟값

"""
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def bfs(ci, cj):
    global shark
    dist = 0
    temp_lst = []
    q = deque()
    visited = [[0]*N for _ in range(N)]
    q.append((ci, cj))
    visited[ci][cj] = 1
    while q:
        i, j = q.popleft()
        if dist == visited[i][j]:
            return temp_lst, dist-1
        for di, dj in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0 and arr[ni][nj] <= shark:
                # 만약 shark가 물고기를 먹을 수 있다면?
                if 0 < arr[ni][nj] < shark:
                    temp_lst.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
                    dist = visited[ni][nj]
                    q.append((ni, nj))
                else:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
    return [], 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ci, cj = 0, 0
# 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            ci, cj = i, j
            arr[i][j] = 0
            break

shark = 2
distance, eat = 0, 0

while True:
    tlst, d = bfs(ci, cj)
    distance += d
    eat += 1
    if shark == eat:
        eat = 0
        shark += 1
    if len(tlst) == 0:
        break
    # x, y 순서로 정렬해야 함
    tlst.sort(key=lambda x: (x[0], x[1]))
    ci, cj = tlst[0]
    arr[ci][cj] = 0
print(distance)
