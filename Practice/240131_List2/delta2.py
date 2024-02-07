N = 5
arr = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                print(arr[ni][nj], end=' ')
        print()