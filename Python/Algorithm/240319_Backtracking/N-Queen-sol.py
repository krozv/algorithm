def f(i, N):
    if i == N:
        return
    else:
        # i 행에 퀸을 놓을 수 있는 조건
        # j 열에 다른 퀸이 없어야 함, 왼쪽 위, 오른쪽 위 대각선 상에도 없어야 함
        for j in range(N):
            if check(i, j, N): # 놓을 수 있으면

def check(i, j, N):
    # 다른 퀸이 있는 지 검사하는 방향
    di = [-1, -1, -1]
    dj = [-1, 0, 1]
    for k in range(3):
        ni, nj = i+di[k], j+dj[k]
        while 

T = int(input())
for t in range(1, T+1):
    N = int(input())

    bd = [[0] * N for _ in range(N)]
