"""
N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산
최소 생산 비용 계산
"""
def cost(r, s):
    global min_cost
    if r == N:
        min_cost = min(s, min_cost)
        return
    if s >= min_cost:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            cost(r+1, s+V[r][i])
            visited[i] = 0


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 99 * N
    visited = [0] * N
    cost(0, 0)
    print(f'#{t} {min_cost}')