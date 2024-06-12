# 미로
"""
N * N 출발지-> 목적지 도착 경로 존재하는 지
도착 1, 아니면 0
"""
def bfs(s):
    x, y = s
    q.append(s)
    v[x][y] = 1
    while q:
        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni = q[0][0] + d[0]
            nj = q[0][1] + d[1]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == 3:
                    return 1
                if v[ni][nj] == 0 and arr[ni][nj] == 0:
                    q.append([ni, nj])
                    v[ni][nj] = 1
        q.pop(0)
    return 0


import sys
sys.stdin = open('input1 (1).txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
                break
    v = [[0]*N for _ in range(N)]
    q = []
    print(f'#{t} {bfs(start)}')

