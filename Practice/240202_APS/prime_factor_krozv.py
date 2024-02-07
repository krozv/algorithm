# 간단한 소인수분해
'''
a, b, c, d, e 출력
2 <= N <= 10,000,000
'''
import sys
sys.stdin = open('input_factorization.txt','r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list = [2, 3, 5, 7, 11]
    factorization = [0] * 5
    for i in range(5):
        while N % num_list[i] == 0:
            N //= num_list[i]
            factorization[i] += 1
    print(f'#{t}', end=' ')
    print(*factorization)