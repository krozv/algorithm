def bfs(x, y):
    global move
    visited[x][y] = 1
    cnt = 1
    person = arr[x][y]
    q = deque()
    q.append([x, y])
    while q:
        for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx = q[0][0] + d[0]
            ny = q[0][1] + d[1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if L <= abs(arr[q[0][0]][q[0][1]] - arr[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    person += arr[nx][ny]
                    cnt += 1
                    q.append([nx, ny])
        q.popleft()

    if cnt > 1:
        move = True
        p = person // cnt
        # 인구 수 변경
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 1:
                    arr[i][j] = p

    if move is None:
        move = False


from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = True
n = 0
while move:
    visited = [[0] * N for _ in range(N)]
    move = None
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                cnt = 1
                person = arr[i][j]
                q = deque()
                q.append([i, j])
                while q:
                    for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        nx = q[0][0] + d[0]
                        ny = q[0][1] + d[1]
                        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                            if L <= abs(arr[q[0][0]][q[0][1]] - arr[nx][ny]) <= R:
                                visited[nx][ny] = 1
                                person += arr[nx][ny]
                                cnt += 1
                                q.append([nx, ny])
                    q.popleft()

                if cnt > 1:
                    move = True
                    p = person // cnt
                    # 인구 수 변경
                    for k in range(N):
                        for l in range(N):
                            if visited[k][l] == 1:
                                arr[k][l] = p

                if move is None:
                    move = False
    if move:
        n += 1
print(n)