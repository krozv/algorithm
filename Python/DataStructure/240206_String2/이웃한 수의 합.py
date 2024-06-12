# 이웃한 수의 합
"""
N개의 정수
이웃한 두 수의 합이 최대인 경우, 최소인 경우 출력
"""
import sys
sys.stdin = open('input_sum.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())    # 5 <= N <= 1000
    num_list = list(map(int, input().split()))
    min_sum = num_list[0] + num_list[1]
    max_sum = num_list[0] + num_list[1]
    for i in range(0, N-1):
        total = num_list[i] + num_list[i+1]
        if min_sum > total:
            min_sum = total
        if max_sum < total:
            max_sum = total
    print(f'#{t} {max_sum} {min_sum}')