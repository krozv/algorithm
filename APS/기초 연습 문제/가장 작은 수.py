# 가장 작은 수
"""
T testcase  1 <= T <= 10
N 정수 개수   5 <= N <= 100,000
num_list 정수 리스트
"""
import sys
sys.stdin = open('in1 (1).txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    min_num = num_list[0]
    min_idx = 1
    for i in range(N):
        if min_num > num_list[i]:
            min_num = num_list[i]
            min_idx = i+1
    print(f'#{t} {min_idx}')