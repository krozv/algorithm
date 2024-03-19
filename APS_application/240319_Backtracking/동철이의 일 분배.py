"""
동철이의 일 분배
N명의 직원, i번
"""
def f(r, s):
    # print(r, s)
    global max_s
    if r == N:
        max_s = max(s, max_s)
        return max_s
    if s <= max_s:
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            f(r+1, s*arr[r][i]*0.01)
            visited[i] = 0

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    max_s = 0
    f(0, 1)
    print(f'#{t} {max_s*100:6f}')
