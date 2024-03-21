# 파이프 옮기기 1
"""
(r, c)로 나타남
번호 1부터 시작함
파이프 회전 가능
N 3<=N<=16
파이프를 (1, 1) -> (N, N)으로 이동시키는 방법의 개수 구하기
하지만 나는 계산하기 귀찮아서 (0, 0) -> (N-1, N-1)로 풀 것임
delta = [[0, 1], [1, 0], [1, 1]]
"""
def dfs(i, j, d):
    global cnt
    deq = deque()
    deq.append([i, j, d])
    while deq:
        x, y, d = deq.popleft()

        if (x, y) == (N-1, N-1):
            cnt += 1
            continue

        if d == 0:
            if y+1 == N:
                continue

            if 0<=x<N and 0<=y+1<N and arr[x][y+1]==0:
                deq.append([x, y+1, 0])

            # 대각선 가기전에 범위 체크해야 함
            if 0<=x<N and 0<=y<N and arr[x][y+1] == 0 and arr[x+1][y] == 0 and arr[x+1][y+1]==0:
                deq.append([x+1, y+1, 2])

        elif d == 1:
            if x+1 == N:
                continue

            if 0 <= x + 1 < N and 0<=y<N and arr[x+1][y]==0:
                deq.append([x+1, y, 1])

            if 0 <= x + 1 < N and 0 <= y+1 < N and arr[x][y+1] == 0 and arr[x+1][y]==0 and arr[x+1][y+1] == 0:
                deq.append([x+1, y+1, 2])

        else:
            if 0 <=x< N and 0 <= y+1< N and arr[x][y + 1] == 0:
                deq.append([x, y+1, 0])

            if 0 <= x + 1 < N and 0 <= y< N and arr[x + 1][y] == 0:
                deq.append([x+1, y, 1])

            if 0 <= x + 1 < N and 0 <= y + 1 < N and arr[x][y + 1] == 0 and arr[x+ 1][y] == 0 and arr[x+1][y+1]==0:
                deq.append([x+1, y+1, 2])



import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs(0, 1, 0)
print(cnt)

