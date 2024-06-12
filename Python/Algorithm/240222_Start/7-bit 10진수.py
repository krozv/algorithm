# 7-bit 10진수
"""
70자리 2진수를 앞에서부터 7비트씩 잘라 10진수로 출력하는 프로그램
"""
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    num = input()
    for n in range(0, 70, 7):
        a = num[n:n+7]
        b = 0
        for i in range(7):
            b += int(a[i]) * 2 ** (6-i)
        print(b, end=' ')
    print()