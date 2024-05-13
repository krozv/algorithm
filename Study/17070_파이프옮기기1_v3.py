import sys

def move_pipes(N, arr):
    for i in range(N):
        for j in range(N):
            if (i, j) == (0, 1):
                arr[i][j] = [0, 0, 1, 0]
            elif arr[i][j] == 1:
                arr[i][j] = [-1, -1, -1, -1]
            else:
                arr[i][j] = [0, 0, 0, 0]

    for i in range(N):
        for j in range(N):
            if arr[i][j][0] > 0:
                if i+1 < N and j+1 < N and all(arr[x][y][0] != -1 for x, y in [(i+1, j), (i, j+1), (i+1, j+1)]):
                    arr[i+1][j+1][0] += arr[i][j][0]
                if j+1 < N and arr[i][j+1][0] != -1:
                    arr[i][j+1][2] += arr[i][j][0]
                if i+1 < N and arr[i+1][j][0] != -1:
                    arr[i+1][j][1] += arr[i][j][0]

            if arr[i][j][1] > 0:
                if i+1 < N and j+1 < N and all(arr[x][y][0] != -1 for x, y in [(i+1, j), (i, j+1), (i+1, j+1)]):
                    arr[i+1][j+1][0] += arr[i][j][1]
                if i+1 < N and arr[i+1][j][0] != -1:
                    arr[i+1][j][1] += arr[i][j][1]

            if arr[i][j][2] > 0:
                if i+1 < N and j+1 < N and all(arr[x][y][0] != -1 for x, y in [(i+1, j), (i, j+1), (i+1, j+1)]):
                    arr[i+1][j+1][0] += arr[i][j][2]
                if j+1 < N and arr[i][j+1][0] != -1:
                    arr[i][j+1][2] += arr[i][j][2]

    return max(sum(arr[N-1][N-1]), 0)

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    input = sys.stdin.readline

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(move_pipes(N, arr))
