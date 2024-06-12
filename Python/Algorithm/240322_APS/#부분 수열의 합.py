import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, s):
    """
    n: 현재까지 고려한 숫자의 개수
    s: 현재까지 더한 숫자의 합
    """
    global cnt
    # 기저조건
    # 1. 현재까지 더한 숫자의 합 = K: cnt += 1, return
    # 2. 현재까지 더한 숫자의 합 > K: return
    # 3. 전체 숫자를 고려함: return
    if s == K:
        cnt += 1
        return
    if s > K:
        return
    if n == N:
        return
    # 재귀
    dfs(n+1, s)
    dfs(n+1, s+arr[n])


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    dfs(0, 0)
    print(f'#{t} {cnt}')