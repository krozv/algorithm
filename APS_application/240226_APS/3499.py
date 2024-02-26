# 투포인트 알고리즘
"""
내꺼
T = int(input())
for t in range(1, T+1):
    N = int(input())
    card = list(input().split())
    a = 0
    b = (len(card)+1) // 2
    print(f'#{t}', end=' ')
    while a < N or b < N:
        if a <= N//2:
            print(card[a], end=' ')
        a += 1
        if b < N:
            print(card[b], end=' ')
        b += 1
    print()

"""
def get_result():
    a = 0
    b = (len(arr)+1) // 2
    print(f'#{t}', end=' ')
    for turn in range(len(arr)):
        if turn % 2 == 0:
            print(arr[a], end=' ')
            a += 1
        else:
            print(arr[b], end=' ')
            b += 1


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    get_result()
    print()

