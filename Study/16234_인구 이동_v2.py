# 16234. 인구 이동

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


# 함수 bfs 정의
def bfs(i, j):
    q = deque()
    q.append([i, j])
    area_lst = []
    population = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = ci+di, cj+dj
            # 범위 내
            if 0<=ni<N and 0<=nj<N and visit[ni][nj] == 0:
                # 인구 이동 가능할 경우
                if L <= abs(arr[ci][cj] - arr[ni][nj]) <= R:
                    visit[ni][nj] = 1
                    q.append([ni, nj])
                    area_lst.append([ni, nj])
                    population += arr[ni][nj]
    return area_lst, population


# 입력
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

flag = True
cnt = 0
while flag:
    flag = False
    cnt += 1
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                # bfs 시작
                area_lst, population = bfs(i, j)
                # 인구 이동 해야 함
                if population:
                    flag = True
                    # 이동한 인구 평균 구하기
                    avg = population // len(area_lst)
                    for area in area_lst:
                        ai, aj = area
                        arr[ai][aj] = avg

print(cnt-1)