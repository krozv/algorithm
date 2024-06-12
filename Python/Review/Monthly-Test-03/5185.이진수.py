# 5185. 이진수
"""
N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램
"""
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, h = input().split()
    N = int(N)
    ans = ''
    for c in h:
        c = int(c, 16)
        ans += str(format(c, '04b'))
    print(f'#{t} {ans}')