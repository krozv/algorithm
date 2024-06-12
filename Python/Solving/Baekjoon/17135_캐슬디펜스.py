# 17135. 캐슬 디펜스
import sys
from itertools import combinations
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def kill(enemy, row, col):
    print(enemy, row, col)
    q = deque()
    q.append((col, row))
    visited = [[0]*M for _ in range(col+1)]
    dis = 0
    while q and dis < D:
        dis += 1
        ci, cj = q.popleft()
        visited[ci][cj] = 1
        if enemy[ci][cj] == 1:
            enemy[ci][cj] = 0
            result = 1
            break
        for di, dj in ((0, -1), (-1, 0), (0, 1)):
            ni, nj = ci+di*dis, cj+dj*dis
            print(ni, nj)
            if 0<=ni<M and 0<=nj<=col and not visited[ni][nj]:
                q.append((ni, nj))
    else:
        result = 0
    return result

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cases = list(combinations(list(range(M)), 3))

max_cnt = 0
for case in cases:
    enemy = arr[:]
    cnt, col = 0, N
    while col > 0:
        enemy = enemy[:col]
        col -= 1
        for row in case:
            cnt += kill(enemy, row, col)
            print(cnt)
    max_cnt = max(max_cnt, cnt)
print(max_cnt)