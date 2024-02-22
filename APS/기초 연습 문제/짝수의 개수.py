# 짝수의 개수
"""
문제
N개의 정수 중 짝수는 몇 개인지 출력
조건
1. T 테스트케이스 1 <= T <= 10
2. N 주어진 정수 5 <= N <= 100000
"""
import sys
sys.stdin = open('in1.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    cnt = 0
    for num in num_list:
        if not num % 2:
            cnt += 1
    print(f'#{t} {cnt}')