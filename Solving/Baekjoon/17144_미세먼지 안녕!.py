class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j


def dust(arr):
    new_arr = [[0]*C for _ in range(R)]
    new_arr[air_cleaner[0]][0] = -1
    new_arr[air_cleaner[1]][0] = -1

    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                cnt = 0
                for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr = r + d[0]
                    nc = c + d[1]
                    if 0<=nr<R and 0<=nc<C and arr[nr][nc] != -1:
                        new_arr[nr][nc] += arr[r][c] // 5
                        cnt += 1
                new_arr[r][c] += arr[r][c] - cnt * (arr[r][c]//5)
    return new_arr


def f(start):
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    ni = start.i + delta[start.dir][0]
    nj = start.j + delta[start.dir][1]
    if nj == 0 and ni in air_cleaner:
        return
    if 0<=ni<R and 0<=nj<C:
        node = Node(ni, nj)
        node.dir = start.dir
        node.dust = arr[ni][nj]
        node.clock = start.clock
        arr[ni][nj] = start.dust
        f(node)
    else:
        node = Node(start.i, start.j)
        if start.clock == 0:
            node.dir = (start.dir+3) % 4
        else:
            node.dir = (start.dir+1) % 4
        node.dust = start.dust
        node.clock = start.clock
        f(node)


import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

air_cleaner = []
for r in range(R):
    if arr[r][0] == -1:
        air_cleaner.append(r)

inlet1 = Node(air_cleaner[0], 0)
inlet1.dir = 1
inlet1.dust = 0
inlet1.clock = 0

inlet2 = Node(air_cleaner[1], 0)
inlet2.dir = 1
inlet2.dust = 0
inlet2.clock = 1

for _ in range(T):
    # 미세먼지 확산
    arr = dust(arr)
    # 공기청정기 작동
    # 위 사이클 - 반시계
    f(inlet1)
    # 아래 사이클 - 시계
    f(inlet2)

s = 0
for r in range(R):
    s += sum(arr[r])
print(s+2)