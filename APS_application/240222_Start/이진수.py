# 이진수 (제출용)
# print(str(bin(0xF)))
# print(ord('A')-55)
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    N, hex_N = input().split()
    for char in hex_N:
        if not char.isdigit():
            num = ord(char) - 55
        else:
            num = int(char)
        b = ''
        for i in range(4):
            b = str(num % 2) + b
            num //= 2
        print(b, end='')
    print()