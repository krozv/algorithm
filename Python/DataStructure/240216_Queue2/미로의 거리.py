# 미로의 거리
"""
N X N 크기 미로, 출발지, 목적지 주어짐
최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는?
경로가 없으면 0개
1은 벽, 0은 통로
"""
def f(coordi):
    output = 0
    x = coordi[0]
    y = coordi[1]
    if coordi == end:
        return visited[x][y]-2
    else:

        q.pop(0)
    if q:
        output = f(q[0])
    return output


import sys
sys.stdin = open('input1.txt', 'r')
T = int(input())
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    start = []
    q = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
                visited[i][j] = 1
                q.append(start)
            if arr[i][j] == 3:
                end = [i, j]

    print(f'#{t} {f(start)}')