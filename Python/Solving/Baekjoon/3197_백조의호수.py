# 3197. 백조의 호수
'''
두 마리의 백조
호수: R * C
호수는 차례대로 녹고, 매일 물과 접촉한 모든 빙판은 녹음
가로나 세로로 닿아있는 경우만
며칠이 지나야 백조가 만날 수 있는가?
함수 2개 필요
1. 얼음 녹이는 함수 bfs
2. 백조 만나는지 체크하는 함수 dfs
'''
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def melting_ice(arr):
    # .이면 물 -> 상하좌우 visited에 체크
    global R, C
    visited = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<R and 0<=nj<C and visited[ni][nj] == 0 and arr[ni][nj] == 'X':
                        visited[ni][nj] = 1

    # 체크된 얼음 물로 변경
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'X' and visited[i][j] == 1:
                arr[i][j] = '.'
    return arr

def is_arrived(i, j):
    global birds
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    # bfs
    while q:
        si, sj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = si + di, sj + dj
            if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0:
                if arr[ni][nj] == '.':
                    q.append([ni, nj])
                    visited[ni][nj] = 1
                if [ni, nj] == birds[1]:
                    return True
    return False


R, C = map(int, input().split())
arr = [list(input().strip('\n')) for _ in range(R)]

# 백조 위치 파악
birds = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'L':
            birds.append([i, j])
si, sj = birds[0]

flag = False
day = 0
while not flag:
    visited = [[0] * C for _ in range(R)]
    flag = is_arrived(si, sj)
    arr = melting_ice(arr)
    day += 1
print(day)
