# 백만 장자 프로젝트
"""

"""
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())    # N: 날짜 2<=N<=1,000,000
    arr = list(map(int, input().split()))
    max_val = arr[-1]
    cnt = 0
    for i in range(N-1, -1, -1):
        if arr[i] > max_val:
            max_val = arr[i]
        elif arr[i] < max_val:
            cnt += max_val - arr[i]

    print(f'#{t} {cnt}')