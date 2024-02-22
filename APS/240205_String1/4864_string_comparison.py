# 4864. 문자열 비교
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = input()
    M = input()
    if N in M:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')