# 숫자를 정렬하자~~~
'''
N길이의 숫자열을 오름차순으로 정렬
5 <= N <= 50
'''
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if num_list[min_idx] > num_list[j]:
                min_idx = j
        num_list[min_idx], num_list[i] = num_list[i], num_list[min_idx]

    print(f'#{t}', end=' ')
    print(*num_list)