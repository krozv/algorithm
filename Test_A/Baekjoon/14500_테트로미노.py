
def f(x, y, n):
    # print(x, y, n)
    global cnt
    delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    path.append([x, y])
    if n == 3:
        path.sort()
        print(path)
        # # print(123, total_path)
        # if path not in total_path:
        #     total_path.append(path)
        #     # print('k', total_path)
        cnt += 1
        return

    for i in range(4):
        # print(i)
        ni = x + delta[i][0]
        nj = y + delta[i][1]
        if 0<=ni<N and 0<=nj<M and [ni, nj] not in path:
            # print(path)
            f(ni, nj, n+1)
            path.pop()


    # q = deque()
    # path
    # q.append([x, y])
    # while q:



import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())    # 4<=N,M<=500
arr = [list(map(int, input().split())) for _ in range(N)]

max_val = 0
total_path = []
path = []
cnt = 0
f(4, 4, 0)
# for i in range(N):
#     for j in range(M):
#         path = []
#         cnt = 0
#         f(i, j, 0)
#
# print(max_val)
print(cnt)
print(total_path)
