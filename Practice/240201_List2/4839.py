# 4839 이진탐색
'''
A, B 중 누가 먼저 페이지 펼치나
이기는 사람 이름 출력
비기면 0
'''
import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    arr = list(range(1, P+1))
    # count A를 구함
    start = 1
    end = P
    count_A = 0
    while start <= end:
        middle = (start + end)//2
        count_A += 1
        if middle == Pa:
            break
        elif middle < Pa:
            start = middle
        else:
            end = middle

    # count B를 구함
    start = 1
    end = P
    count_B = 0
    while start <= end:
        middle = (start + end)//2
        count_B += 1
        if middle == Pb:
            break
        elif middle < Pb:
            start = middle
        else:
            end = middle
    if count_A == count_B:
        print(f'#{t} 0')
    elif count_A > count_B:
        print(f'#{t} B')
    else:
        print(f'#{t} A')



