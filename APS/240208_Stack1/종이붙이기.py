# 종이붙이기
"""
가로 세로 길이 10x20, 20x20
f(n) = f(n-1) + 2 * f(n-2)
"""
T = int(input())
for t in range(1, T+1):
    N = int(input()) // 10
    memo = [0] * (N+1)
    memo[1] = 1
    memo[2] = 3
    for i in range(3, N+1):
        memo[i] = memo[i-1] + 2* memo[i-2]
    print(f'#{t} {memo[N]}')