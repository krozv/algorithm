# 이진수 표현
"""
N, M 이 주어질 때 M의 이진수 표현의 마지막 N비트가 모두 1로 ~~
"""
import sys
sys.stdin = open('input.txt', 'r')
'''
내 코드
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    for i in range(N):
        if not 1 & M >> i:
            print(f'#{t} OFF')
            break
    else:
        print(f'#{t} ON')
'''
'''
창디 코드
'''
T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    print()
    if m & (1 << n)-1 == (1 << n)-1:
        print(f"#{tc+1} ON")
    else:
        print(f"#{tc+1} OFF")
