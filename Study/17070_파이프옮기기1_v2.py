# 17070. 파이프 옮기기1
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if (i, j) == (0, 1):
            arr[i][j] = [0, 0, 1, 0]
            continue
        if arr[i][j] == 1:
            arr[i][j] = [-1, -1, -1, -1]
            continue
        arr[i][j] = [0, 0, 0, 0]

for i in range(N):
    for j in range(N):
        # 일단 적고 범위 나중에 처리하자
        # 대각선
        if arr[i][j][0] > 0:
            if i+1 < N and j+1 < N and arr[i+1][j+1][0] != -1 and arr[i][j+1][0] != -1 and arr[i+1][j][0] != -1:
                arr[i+1][j+1][0] += arr[i][j][0]
            if j+1 < N and arr[i][j+1][0] != -1:
                arr[i][j+1][2] += arr[i][j][0]
            if i+1 < N and arr[i+1][j][0] != -1:
                arr[i+1][j][1] += arr[i][j][0]

        # 세로
        if arr[i][j][1] > 0:
            if i+1 < N and j+1 < N and arr[i+1][j+1][0] != -1 and arr[i][j+1][0] != -1 and arr[i+1][j][0] != -1:
                arr[i+1][j+1][0] += arr[i][j][1]
            if i+1 < N and arr[i+1][j][0] != -1:
                arr[i+1][j][1] += arr[i][j][1]

        # 가로
        if arr[i][j][2] > 0:
            if i+1 < N and j+1 < N and arr[i+1][j+1][0] != -1 and arr[i][j+1][0] != -1 and arr[i+1][j][0] != -1:
                arr[i+1][j+1][0] += arr[i][j][2]
            if j+1 < N and arr[i][j+1][0] != -1:
                arr[i][j+1][2] += arr[i][j][2]

# 출력 확인용
result = sum(arr[N-1][N-1])
if result < 0:
    result = 0
print(result)