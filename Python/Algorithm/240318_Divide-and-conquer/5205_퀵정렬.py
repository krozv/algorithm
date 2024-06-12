"""
퀵 정렬 구현
"""
def quick_sort(m, l, r):
    if l < r:
        s = partition(m, l, r)
        quick_sort(m, l, s - 1)
        quick_sort(m, s+1, r)


def partition(m, l, r):
    p = m[l]
    i, j = l, r
    while i <= j:
        while i <= j and m[i] <= p:
            i += 1
        while i <= j and m[j] >= p:
            j -= 1
        if i < j:
            m[i], m[j] = m[j], m[i]
    m[l], m[j] = m[j], m[l]
    return j

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N-1)
    print(f'#{t} {arr[N//2]}')