# 토너먼트 카드게임
"""
N명의 학생이 N장의 카드를 나눠 갖는다.
두 그룹으로 나눈다
그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다 -> N이 홀수일 때 부전승 존재
그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑느다
1 < 2, 2 < 3, 1 > 3
N명의 학생들이 카드를 골랐을 때 1등을 찾는 프로그램을 만드시오
"""


def f(arr, N):
    """
    arr: 번호
    N: 들고 있는 카드 개수
    """
    if N == 2:
        if card[arr[0]] + card[arr[1]] == 4 and card[arr[0]] != card[arr[1]]:
            if card[arr[0]] < card[arr[1]]:
                return [arr[0]], 1
            else:
                return [arr[1]], 1
        else:
            if card[arr[0]] < card[arr[1]]:
                return [arr[1]], 1
            else:
                return [arr[0]], 1
    if N == 1:
        return arr, 1

    else:
        if N % 2:
            A = arr[:N//2+1]
            B = arr[N//2+1:]
            arr1, N1 = f(A, N//2+1)
            arr2, N2 = f(B, N//2)
            return f(arr1+arr2, N1+N2)     # 홀수 및 짝수에 따라 개수가 다름 -> 어떻게 표시할 건지 고민할 것!!!!!!!!
        else:
            A = arr[:N//2]
            B = arr[N//2:]
            arr1, N1 = f(A, N // 2)
            arr2, N2 = f(B, N//2)
            return f(arr1+arr2, N1+N2)


import sys
sys.stdin = open('input1.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    num = list(range(N))
    winner, _ = f(num, N)
    print(f'#{t} {winner[0]+1}')