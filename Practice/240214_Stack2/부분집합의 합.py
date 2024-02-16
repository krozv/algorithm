# 부분집합의 합
"""
1~12까지의 숫자를 원소로 가진 집합 A
N개의 원소, K가 합인 부분집합의 개수 출력
없으면 0
"""
def f(i, n, k):
    """
    i: 현재 탐색한 원소의 개수
    n: 배열의 원소 개수
    k: 목표하는 합
    """
    global subset
    # 전체 탐색한 것
    if i == n:
        ss = 0
        for j in range(12):
            if bit[j]:
                ss += A[j]
        if ss == k:
            if sum(bit) == N:
                subset += 1

    else:
        bit[i] = 0
        f(i+1, n, k)
        bit[i] = 1
        f(i+1, n, k)


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    bit = [0] * 12
    subset = 0
    f(0, 12, K)
    print(f'#{t} {subset}')