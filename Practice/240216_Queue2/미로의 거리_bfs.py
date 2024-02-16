"""
dfs 제대로 이해하기...!
"""
def bfs(s, e):
    """
    s: 시작지점
    e: 도착지점
    """
    # q 생성
    q = []
    # 시작점 인큐
    x = s[0]
    y = s[1]
    q.append(s)
    # 인큐 표시
    visited[x][y] = 1
    # q에 정점이 남아있으면
    while q:
        # 디큐
        t = q.pop(0)
        if t == e:
            return visited[t[0]][t[1]] - 2
        for k in range(4):
            ni = t[0] + di[k]
            nj = t[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[t[0]][t[1]] + 1
    return 0

"""
정점 찾는 코드
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
for k in range(4):
    ni = x + di[k]
    nj = y + dj[k]
    if 0 <= ni < N and 0 <= nj < N:
        if arr[ni][nj] != 1 and visited[ni][nj] == 0:
            visited[ni][nj] = visited[x][y] + 1
            q.append([ni, nj])
"""

import sys
sys.stdin = open('input1.txt', 'r')
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    start = end = 0

    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
            if arr[i][j] == 3:
                end = [i, j]

    print(f'#{t} {bfs(start, end)}')