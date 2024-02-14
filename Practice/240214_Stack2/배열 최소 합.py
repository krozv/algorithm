# 배열 최소 합
"""
배열에 숫자가 들어있음 (숫자는 자연수)
한 줄에서 N개씩 숫자를 골라 합이 최소가 되려고 함 -> 약간 스도쿠 같음
백트래킹으로 풀 것
"""
def f(i, k, s):
    """
    i: 현재 고려한 원소의 개수
    k: 총 원소 개수
    s: 부분집합의 합
    손으로 그려서 풀어보기,,,
    """
    global min_val
    # 모든 원소를 고려하였을 경우, i == k
    if i == k:
        # 밑에 3줄을 넣었을 때 실행시간 배로 차이남.. -> 왜...?
        # s = 0
        # for j in range(k):
        #     s += arr[j][p[j]]
        if min_val > s:
            min_val = s
    # 고려할 필요도 없는 경우 (예: 최솟값보다 s가 큰 경우)
    elif s > min_val:
        return
    # 계속 고려 중,,,
    else:
        for j in range(i, k):
            print(p)
            p[i], p[j] = p[j], p[i]
            f(i+1, k, s+arr[i][p[i]])
            p[i], p[j] = p[j], p[i]


import sys
sys.stdin = open('input1.txt', 'r')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]   # 겹치지 않도록 크기가 같은 배열을 만듦
    min_val = 100
    f(0, N, 0)
    print(f'#{t} {min_val}')