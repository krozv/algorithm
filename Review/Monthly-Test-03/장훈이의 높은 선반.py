# 장훈이의 높은 선반
import sys
sys.stdin = open('input.txt', 'r')
def f(n, s):
    """
    n: 현재까지 포함 여부를 결정한 직원의 숫자
    s: 현재까지 포함한 키의 합
    """
    # 백트래킹
    global sub
    # 키의 합 > B인 경우
    if s >= B:
        sub = min(sub, s - B)
        return
    # 모든 점원을 다 체크한 경우
    if n == N:
        return
    # 재귀
    f(n+1, s)
    f(n+1, s+arr[n])


T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    sub = sum(arr)
    f(0, 0)
    print(f'#{t} {sub}')