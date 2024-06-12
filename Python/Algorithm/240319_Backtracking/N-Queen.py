def chess(n, x, y):
    # print(n ,x, y)
    # chess를 다 놓았을 경우
    if n == N:
        print('path', path)
        return

    # 일단 체스 둬
    arr[x][y] = 1
    path.append([x, y])

    # 벽 세워
    # 행
    for k in range(N):
        if k != y and arr[x][k] != 2:
            arr[x][k] = 1
    # 열
    for k in range(N):
        if k != x and arr[k][y] != 2:
            arr[k][y] = 1
    # 대각선
    for d in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
        for k in range(1, N):
            dx = x + d[0] * k
            dy = y + d[1] * k
            if 0<=dx<N and 0<=dy<N and arr[dx][dy] != 2:
                arr[dx][dy] = 1
    print(arr)
    # 다음 체스 두러 가
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and [i, j] not in path:
                chess(n+1, i, j)
    # 벽 무너뜨리기
    # 행
    for k in range(N):
        if k != y and arr[x][k] == 1:
            arr[x][k] = 0
    # 열
    for k in range(N):
        if k != x and arr[k][y] == 1:
            arr[k][y] = 0
    # 대각선
    for d in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
        for k in range(1, N):
            dx = x + d[0] * k
            dy = y + d[1] * k
            if 0 <= dx < N and 0 <= dy < N and arr[dx][dy] == 1:
                arr[dx][dy] = 0
    arr[x][y] = 0

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            path = []
            chess(0, i, j)
    print()
