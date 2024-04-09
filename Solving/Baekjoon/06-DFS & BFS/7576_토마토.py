# 7576. 토마토
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def bfs():
    q = deque()
    q.extend(tomato)
    while q:
        i, j, t = q.popleft()
        global time
        time = t
        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj, nt = i+d[0], j+d[1], t+1
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                arr[ni][nj] = 1
                q.append([ni, nj, nt])


def test():
    # tomato 검사
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return False
    else:
        return True


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = test()

if result:
    print(0)
else:
    tomato = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                tomato.append([i, j, 0])
    time = 0
    bfs()
    result = test()
    if result:
        print(time)
    else:
        print(-1)
