# 디저트 카페
def bfs(i, j):
    global max_val
    q = [[i, j, 0]]
    visited = [[0] * N for _ in range(N)]
    path = [arr[i][j]]
    # print(q)
    while q:
        print(q)
        if q[0][-1] > 3:
            q.append([q[0][0]-delta[q[0][-1]][0], q[0][1]-delta[q[0][-1]][1], 0])
            continue
        ni = q[0][0] + delta[q[0][-1]][0]
        nj = q[0][1] + delta[q[0][-1]][1]
        # 범위 내
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
            if (ni, nj) not in [(0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)]:
                if [ni, nj] == start:
                    print(i,j,path)
                    if max_val < len(path):
                        max_val = len(path)
                    return
                if arr[ni][nj] not in path:
                    visited[ni][nj] = 1
                    q.append([ni, nj, q[0][-1]])
                    path.append(arr[ni][nj])
                else:
                    visited[ni][nj] = 1
                    q.append([ni-delta[q[0][-1]][0], nj-delta[q[0][-1]][1], q[0][-1]+1])
        # 범위 밖
        else:
            q.append([ni-delta[q[0][-1]][0], nj-delta[q[0][-1]][1], q[0][-1]+1])
        q.pop(0)


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    delta = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    max_val = 0
    for i in range(N):
        for j in range(N):
            if (i, j) not in [(0, 0), (0, N-1), (N-1, 0), (N-1, N-1)]:
                start = [i, j]
                bfs(i, j)
    if not max_val:
        print(f'#{t} -1')
    else:
        print(f'#{t} {max_val}')