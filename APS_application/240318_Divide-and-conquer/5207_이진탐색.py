"""
리스트 B에 들어있는 정수 M개가 리스트 A에 들어있는 지 이진 탐색을 통해 확인
B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과저에서 양쪽구간을 번갈아 선택하는 지!!
"""

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    A.sort()
    for num in B:
        l = 0
        r = N-1
        left, right = 1, 1
        while l <= r:
            m = (l+r)//2
            print(A[l], A[m], A[r])
            if A[m] == num:
                cnt += 1
                break
            if A[m] < num and right:
                l = m + 1
                left, right = 1, 0
            elif A[m] > num and left:
                r = m - 1
                left, right = 0, 1
            else:
                break
    print(f'#{t} {cnt}')
