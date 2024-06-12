import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 1<=N<=100, 1<=K<=100,000
info = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K+1)

for W, V in info:
    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i-W]+V)

print(dp[K])