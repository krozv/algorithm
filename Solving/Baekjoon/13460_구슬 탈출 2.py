# 13460. 구슬 탈출 2
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dfs(start, d):
    i, j = start
    visit[i][j] = 1
    pass


N, M = map(int, input().split())
arr = [list(input().strip('\n')) for _ in range(N)]

hole = ''
red = ''
blue = ''
# 구멍, 빨간 구슬, 파란 구슬 위치 찿기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'O':
            hole = [i, j]
        elif arr[i][j] == 'R':
            red = [i, j]
        elif arr[i][j] == 'B':
            blue = [i, j]
print(hole, red, blue)

# dfs or 반복문
visit = [[0] * M for _ in range(N)]
dfs(hole, 0)