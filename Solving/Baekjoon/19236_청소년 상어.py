# 청소년 상어
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


# class Fish:
#     def __init__(self, num, dir, now):
#         self.num = num
#         self.dir = dir
#         self.prev = self.now = now
#
#     def move(self):
#         delta = [0, (0, -1), (-1, -1), (-1, 0), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
#         i, j = self.now
#         ni, nj = i+delta[self.dir][0], j+delta[self.dir][1]
#         # 100 == shark
#         if 0<=ni<4 and 0<=nj<4 and arr[ni][nj] != 100:
#             self.prev = [i, j]
#             self.now = [ni, nj]
#         else:
#             self.dir = (self.dir + 1) % 8


f = [list(map(int, input().split())) for _ in range(4)]
arr = [[0]*4 for _ in range(4)]
fishes_dir = [0] * 17
for i in range(4):
    for j in range(4):
        arr[i][j] = f[i][j*2]
        fishes_dir[arr[i][j]] = f[i][j*2+1]
# 상어가 물고기 먹음
# 상어 == 100
fishes_dir[arr[0][0]] = 0
arr[0][0] = 100
eat = arr[0][0]
shark
# 물고기 이동
