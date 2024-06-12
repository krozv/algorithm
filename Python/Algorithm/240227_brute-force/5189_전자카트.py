# 5189. 전자카드
"""
한칸당 하나씩만 고르는데 (1, 1), (2, 2) ... (N, N)은 못감
최솟값?
"""
def f(x, i, s):
    """
    x: 몇번 돌았는지
    i: 지금 도착한 장소
    s: 지금까지 배터리 총합
    """
    global min_s
    # back tracking
    if s > min_s:
        return
    # base case
    if x == N-1:
        s += arr[i][0]
        if min_s > s:
            min_s = s
        return

    for j in range(N):
        if not visited[j] and i != j:
            visited[j] = 1
            f(x+1, j, s+arr[i][j])
            visited[j] = 0


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [1] + [0] * (N-1)
    min_s = 100 * N * 2
    f(0, 0, 0)
    print(f'#{t} {min_s}')