# 당근 수확
"""
당근밭 N개의 구역
첫번째 일꾼 1 ~ x
두번째 일꾼 x+1 ~ N
수확한 당근 개수의 차이가 최소가 되도록
남겨 놓는 당근 X
여러 영역 가능한 경우 가장 빠른 번호
"""
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())    # 1<=T<=50
for t in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    human1 = 0
    human2 = 0
    min_sub = 10    # 가능한 가장 큰 당근 개수의 차이 [0, 0, 0, 0, 10]
    min_idx = 1
    for carrot in carrots:
        human2 += carrot

    for i in range(N-1):
        human1 += carrots[i]
        human2 -= carrots[i]
        if human1 > human2:
            sub = human1 - human2
            idx = i+1
        else:
            sub = human2 - human1
            idx = i+1
        if min_sub > sub:
            min_sub = sub
            min_idx = idx
    print(f'#{t} {min_idx} {min_sub}')

