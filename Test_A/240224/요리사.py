# 요리사
"""
N개의 식재료
식재료를 N/2개씩 나누어 두 개의 요리 (N 짝수)
A음식, B음식
맛의 차이가 최소가 되도록 재료 배분
"""
def g(n, i):
    if i == len(n):
        return
    print(i, n)
    n[i], n[i+1] = n[i+1], n[i]
    g(n, i+1)
    n[i], n[i+1] = n[i+1], n[i]

def f(n):
    if sum(bit) == N//2:
        A = []
        B = []
        for i in range(N):
            if bit[i]:
                A.append(i)
            else:
                B.append(i)
        g(A, 0)
        return
    if n == N:
        return
    bit[n] = 0
    f(n+1)
    bit[n] = 1
    f(n+1)

import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] += arr[j][i]
    bit = [0] * N

    A = []
    B = []
    f(0)

