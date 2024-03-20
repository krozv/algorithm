# 5247. 연산
"""
조건
1. 연산 종류 4가지
2. 연산의 중간 결과도 백만 이하의 자연수
"""
def f(N, cnt):
    global min_cnt
    print(N, cnt)
    if N == M:
        if min_cnt == 0:
            min_cnt = cnt
        min_cnt = min(min_cnt, cnt)
        return

    if min_cnt and cnt >= min_cnt:
        return

    if N >= 1e6 or N <= 0:
        return
    # 2**n이 M 근처에 올 때까지 -> f(N * 2)
    # 123456

    f(N + 1, cnt + 1)
    f(N - 1, cnt + 1)
    f(N - 10, cnt + 1)
    f(N * 2, cnt + 1)



import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    min_cnt = 0
    f(N, 0)
    print(f'#{t} {min_cnt}')