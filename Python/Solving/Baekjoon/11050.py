# 11050. 이항 계수1

import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    memo = [1] * 11

    for i in range(2, 11):
        memo[i] = memo[i-1] * i 

    if 0 <= k <= n:
        return memo[n] / (memo[k] * memo[n-k])
    else:
        return 0


if __name__ == "__main__":
    print(int(solution()))