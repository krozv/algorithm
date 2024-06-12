# 최대 상금
"""
왼쪽으로 갈수록 10의 배수
즉 현재 위치한 카드 위치 = 금액
가장 큰 금액 출력
"""
def f(i, a):
    """
    i: 현재까지 교환한 횟수
    a: 교환한 자리의 인덱스
    """
    print(i, a)
    print(arr)
    if i == N:
        print('end')
        return
    max_idx = len(arr) - 1

    if arr == op_arr:
        print('optimization')

    else:
        for j in range(len(arr)-1, a-1, -1):
            if arr[max_idx] < arr[j]:
                max_idx = j
        print('max_idx:', max_idx)
        if max_idx == a:
            f(i, a+1)
        else:
            arr[a], arr[max_idx] = arr[max_idx], arr[a]
            f(i+1, a+1)





import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    print('--------------')
    arr, N = input().split()
    N = int(N)
    arr = list(map(int, list(arr)))
    op_arr = sorted(arr, reverse=True)
    f(0, 0)
