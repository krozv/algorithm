# 17135. 캐슬 디펜스
import sys
from itertools import combinations
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def kill(enemy, bow, row):
    q = deque()
    q.append((row, bow))
    visited = [[0]*M for _ in range(row+1)]
    visited[row][bow] = 1
    while q:
        ci, cj = q.popleft()

        if visited[ci][cj] > D:
            break

        if enemy[ci][cj] == 1:
            return (ci, cj)

        for r in range(0, visited[ci][cj]+1):
            c = visited[ci][cj]-r
            ni, nj = row-r, bow-c
            if 0<=ni<=row and 0<=nj<M and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1

        for r in range(visited[ci][cj]-1, -1, -1):
            c = visited[ci][cj] - r
            ni, nj = row-r, bow+c
            if 0<=ni<=row and 0<=nj<M and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1

    return 0


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cases = list(combinations(list(range(M)), 3))

max_cnt = 0
for case in cases:
    enemy = [a[:] for a in arr]
    cnt, row = 0, N
    while row > 0:
        enemy = enemy[:row]
        row -= 1
        killed_enemies = set()
        for bow in case:
            loc = kill(enemy, bow, row)
            if loc:
                killed_enemies.add(loc)
        for killed in killed_enemies:
            enemy[killed[0]][killed[1]] = -1
            cnt += 1
    max_cnt = max(max_cnt, cnt)

print('답:', max_cnt)