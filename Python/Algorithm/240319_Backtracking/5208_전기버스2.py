"""
최소한의 교체 횟수로 목적지에 도착
출발지 배터리 장착은 제외
"""
def charge(b, c, n):
    global min_c
    if b < 0 or c >= min_c:
        return

    # 종점에 도착
    if n == N:
        print(c)
        min_c = min(min_c, c)
        return min_c

    # 배터리 교체할 지 여부
    charge(arr[n]-1, c+1, n+1)
    charge(b-1, c, n+1)


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    min_c = N-1
    charge(arr[1]-1, 0, 2)
    print(f'#{t} {min_c}')
