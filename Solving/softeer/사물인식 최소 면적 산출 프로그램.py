import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
arr = [[[] for _ in range(2001)]for _ in range(2001)]  # 2001 * 2001 배열
for _ in range(N):
    x, y, k = map(int, input().split())
    arr[x+1000][y+1000].append(k)
    print(arr[x+1000][y+1000])
visited = [0] * (K+1)
# 완전탐색하는 부분 다시 짜세용
for d in range(2000):
    for i in range(2001):
        for j in range(2001):
            if arr[i][j]:
                for color in arr[i][j]:
                    visited[color] = 1
            if not visited.count(0):
                break
