# 5188. 최소합
"""
N * N 칸에 숫자가 적힌 칸 주어짐
최소합계를 출력
완전탐색 + 재귀
"""
def start(i, j, s):
    global min_val
    if s > min_val:
        return
    if i == N or j == N:
        return
    if (i, j) == (N-1, N-1):
        s += arr[i][j]
        if min_val > s:
            min_val = s
        return
    if not visited[i][j]:
        visited[i][j] = 1
        start(i+1, j, s+arr[i][j])
        start(i, j+1, s+arr[i][j])
        visited[i][j] = 0


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    min_val = 10 * N * 2
    start(0, 0, 0)
    print(f'#{t} {min_val}')