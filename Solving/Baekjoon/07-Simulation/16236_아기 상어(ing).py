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


def bfs(start):
    q = deque()
    q.append(start)
    while q:
        print(q)
        i, j, shark, fish = q.popleft()
        if shark == fish:
            shark += 1
        visit[i][j] = shark
        for d in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
            ni = i + d[0]
            nj = j + d[1]
            if 0<=ni<N and 0<=nj<N and not visit[ni][nj]:
                if arr[ni][nj] == shark:
                    q.append([ni, nj, shark, fish])
                elif 0 < arr[ni][nj] < shark:
                    arr[ni][nj] = 0
                    q.append([ni, nj, shark, fish+1])
                elif arr[ni][nj] == 0:
                    q.append([ni, nj, shark, fish])



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
baby = []
# 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            baby = [i, j, 2, 0]
            break

visit = [[0]*N for _ in range(N)]
bfs(baby)
print(arr)