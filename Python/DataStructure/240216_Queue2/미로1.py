# 미로1
def bfs(s):
    """
    s: 시작지점
    """
    # 큐랑 방명록 만들어야함
    q = [s]
    v = [[0]*N for _ in range(N)]

    while q:
        c = q.pop(0)    # 현재위치
        x = c[0]
        y = c[1]
        if arr[x][y] == 3:
            return 1
        for d in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni = x + d[0]
            nj = y + d[1]
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append([ni, nj])
                v[ni][nj] = 1
    return 0

# 입력
T = 10
for t in range(1, T+1):
    _ = input()
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
                print(f'#{t} {bfs(start)}')
                break